# -*- coding: utf-8 -*-

from main import app
from auth import auth

from db.Lib import LibManager
from flask import session, render_template, url_for, redirect, request

import json


@app.route("/", methods=["GET"])
@auth
def index():
    lib = LibManager()
    cards = lib.getCards(session["uid"])
    print cards
    return render_template("index.html", cards=cards)

@app.route("/test", methods=["GET"])
def testcard():
    session["uid"] = 1
    return "test"

@app.route("/hascard/<int:tuid>", methods=["GET"])
@auth
def hascard(tuid):
    if tuid == 0:
        return "false"
    lib = LibManager()
    return json.dumps(lib.hasCard(session["uid"], tuid))


@app.route("/clear", methods=["GET"])
def clear():
    session.clear()
    return "clear"
