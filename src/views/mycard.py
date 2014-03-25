# -*- coding: utf-8 -*-

from main import app
from auth import auth
from flask import request, session, redirect, url_for, render_template, flash

from db.Card import CardManager

import json

@app.route("/mycard", methods=["GET"])
@auth
def mycard_redirect():
    return redirect(url_for("card", uid=session["uid"]))

@app.route("/edit", methods=["GET"])
@auth
def editcard():
    uid = session["uid"]
    cardManager = CardManager()
    card = cardManager.getCardByUid(uid)
    return render_template("edit.html", card=card)

@app.route("/set", methods=["POST"])
@auth
def setcard():
    if request.method == "POST":
        cardManager = CardManager()

        uid = session["uid"]
        name = request.form["name"]
        info = request.form["info"]
        phone = request.form["phone"]
        email = request.form["email"]
        card = cardManager.getCardByUid(uid)

        error = ""

        if(cardManager.getCardByUid(uid)):
            cardManager.updateCard(uid, name, info, phone, email)
        else:
            if not cardManager.insertCard(uid, name, info, phone, email):
                error = u"编辑失败"
        if error:
            flash(error)
            return "false"
        return "true"

@app.route("/get", methods=["GET"])
@auth
def get_redirect():
    uid = session["uid"]
    return redirect(url_for("getcard", uid=uid))


@app.route("/get/<int:uid>", methods=["GET"])
@auth
def getcard(uid):
    if request.method == "GET":
        cardManager = CardManager()
        card = cardManager.getCardByUid(uid)
        if card:
            card["result_code"] = 1
            return json.dumps(card, ensure_ascii=False)
        else:
            return str({"result_code" : 0})

