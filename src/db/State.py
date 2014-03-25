# -*- coding: utf-8 -*-

import hashlib

from MySQLdb import IntegrityError

try:
    from db.db_conn import get_db
except:
    import MySQLdb
    def get_db():
        return MySQLdb.connect("localhost", "user", "", "cards")

class StateManager(object):
    def __init__(self):
        self._conn = get_db()

    def getState(self, url):
        return hashlib.sha256(url).hexdigest()[-8:]

    def insertState(self, url, state=""):
        if not state:
            state = self.getState(url)
        cur = self._conn.cursor()
        sql = "INSERT State(state, url) values(%s, %s)"
        try:
            if cur.execute(sql, (state, url)) == 1:
                self._conn.commit()
                return True
            return False
        except IntegrityError, e:
            from tools.log import writelog
            import traceback
            writelog(e)
            writelog(traceback.format_exc())
            self._conn.rollback()
            return False
    def getStateByUrl(self, url):
        cur = self._conn.cursor()
        sql = "SELECT state FROM State WHERE url=%s"
        if cur.execute(sql, (url,)) > 0:
            return cur.fetchone()[0]
        return None

    def getUrlByState(self, state):
        cur = self._conn.cursor()
        sql = "SELECT url FROM State WHERE state=%s"
        if cur.execute(sql, (state,)) > 0:
            return cur.fetchone()[0]
        return None
