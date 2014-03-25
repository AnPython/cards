# -*- coding: utf-8 -*-

import MySQLdb
from main import app
from flask import g

db_addr = app.config["MYSQL_ADDRESS"]
db_name = app.config["MYSQL_DBNAME"]
db_user = app.config["MYSQL_USERNAME"]
db_pass = app.config["MYSQL_PASSWORD"]
db_port = int(app.config["MYSQL_PORT"])

def get_db():
    if not hasattr(g, "db_conn"):
        g.db_conn = MySQLdb.connect(host=db_addr, port=db_port,
                            user=db_user, passwd=db_pass, db=db_name, charset="utf8")
    return g.db_conn

@app.teardown_appcontext
def db_close(error):
    if hasattr(g, "db_conn"):
        g.db_conn.close()
