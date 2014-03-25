from main import app
from auth import auth

from flask import request, render_template, session

from db.Lib import LibManager
from db.User import UserManager
from db.Card import CardManager

@app.route("/card/<int:uid>", methods=["GET"])
@auth
def card(uid):
    myuid = session["uid"]

    cardManager = CardManager()
    card = cardManager.getCardByUid(uid)
    if(uid == myuid):
        error = request.args.get("error", "")
        if card == None:
            card = {"uid": uid,
                    "name" : "",
                    "info" : "",
                    "email" : "",
                    "phone" : ""
                    }
        return render_template("mycard.html", card=card, error=error)
    else:
        if card:
            return render_template("card.html", card=card)
        else:
            return "false"

@app.route("/add/<int:tuid>", methods=["GET"])
@auth
def addcard(tuid):
    lib = LibManager()
    user = UserManager()
    uid = session["uid"]
    result = "false"
    if user.hasUid(tuid) and not lib.hasCard(uid, tuid):
        if lib.addCard(uid, tuid):
            result = "true"
    return result

@app.route("/del/<int:tuid>", methods=["GET"])
@auth
def delcard(tuid):
    lib = LibManager()
    user = UserManager()
    uid = session["uid"]

    result = "false"
    if user.hasUid(tuid) and lib.hasCard(uid, tuid):
        if lib.deleteCard(uid, tuid):
            result = "true"
    return result
