# -*- coding: utf-8 -*-

from main import app
from auth import auth
from flask import session, request, redirect, url_for

from tools.weixin import weixin_auth, Message
from db.Message import MessageManager

@app.route("/weixin", methods=["GET", "POST"])
def weixin():
    auth_info = []
    sign = request.args.get("signature", "")
    echostr = request.args.get("echostr", "")
    time = request.args.get("timestamp", "")
    nonce = request.args.get("nonce", "")
    if weixin_auth(sign, time, nonce):
        msg = Message(request.data)
        manager = MessageManager()
        #return msg.dump_textmsg(msg.get_dict()["Content"])
        if manager.insertMessage(msg):
            return msg.dump_textmsg(u"已收到您的反馈，谢谢")
        else:
            return msg.dump_textmsg(u"系统繁忙，请稍后发送")
    else:
        return "weixin"
        return redirect(url_for("index"))
