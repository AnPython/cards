# -*- coding: utf-8 -*- 
from main import app
from auth import auth
from flask import request, redirect, url_for, session

from db.User import UserManager
from db.State import StateManager

import urllib

@app.route("/oauth", methods=["GET"])
def oauth():
    if request.method == "GET":
        referrer = request.args.get("referrer", "")

        #从数据库查找state
        stateManager = StateManager()
        state = stateManager.getStateByUrl(referrer)

        #如果state为空，则生成state
        if state == None:
            if stateManager.insertState(referrer):
                state = stateManager.getStateByUrl(referrer)
            else:
                return u"生成state失败"

        para = {"appid" : app.config["APPID"],
                "redirect_uri" : app.config["BASE_URL"] + url_for("gettoken"),
                "response_type" : "code",
                "scope" : "snsapi_base",
                "state" : state,
                }
        oauth_url = "https://open.weixin.qq.com/connect/oauth2/authorize?%s#wechat_redirect"

        """重定向到Weixin Oauth2"""
        return redirect(oauth_url % urllib.urlencode(para))

@app.route("/gettoken", methods=["GET"])
def gettoken():
    if request.method == "GET":
        state = request.args.get("state", "")
        code = request.args.get("code", "")
        if code:
            url = "https://api.weixin.qq.com/sns/oauth2/access_token?"
            para = {"appid" : app.config["APPID"],
                    "secret" : app.config["APPSECRET"],
                    "code" : code,
                    "grant_type" : "authorization_code",
                    }

            try_time = 0
            while(try_time<3):
                url += urllib.urlencode(para)
                content = urllib.urlopen(url).read()
                if content:
                    break
            else:
                return u"获取token失败"

            info = eval(content)
            try:
                openid = info["openid"]
            except KeyError:
                openid = ""

            #openid为空则返回错误
            if not openid:
                return "获取openid失败, url=%s" % url

            userManager = UserManager()
            uid = userManager.getUidByOpenID(info["openid"])

            if uid:
                session["uid"] = uid
            else:
                userManager.insertUser(info)
                uid = userManager.getUidByOpenID(info["openid"])
                session["uid"] = uid

            stateManager = StateManager()
            url = stateManager.getUrlByState(state)
            return redirect(url)
        else:
            return u"获取code失败"
