# -*- coding: utf-8 -*-

from db.db_conn import get_db

class UserManager(object):
    def __init__(self):
        self._conn = get_db()

    def insertUser(self, info):
        try:
            cur = self._conn.cursor()
            sql = "INSERT User(openid, access_token, refresh_token, \
                               expires_in, scope) \
                    values(%s, %s, %s, %s, %s)"
            cur.execute(sql, (info["openid"], info["access_token"],
                              info["refresh_token"], info["expires_in"],
                              info["scope"]))
            self._conn.commit()
            return True
        except Exception, e:
            import traceback
            print e
            print traceback.format_exc()
            self._conn.rollback()
            return False
    def hasUid(self, uid):
        cur = self._conn.cursor()
        sql = "SELECT uid FROM User WHERE uid=%s"
        if cur.execute(sql, (uid,)) > 0:
            return True
        return False

    def getOpenIDByUid(self, uid):
        try:
            cur = self._conn.cursor()
            sql = "SELECT openid FROM User WHERE uid=%s"
            if cur.execute(sql, (uid,)) > 0:
                return cur.fetchone()[0]
            return None
        except Exception, e:
            import traceback
            print e
            print traceback.format_exc()
            return None

    def getUidByOpenID(self, openid):
        try:
            cur = self._conn.cursor()
            sql = "SELECT uid FROM User WHERE openid=%s"
            if cur.execute(sql, (openid,)) > 0:
                return cur.fetchone()[0]
            return None
        except Exception, e:
            import traceback
            print e
            print traceback.format_exc()
            return None
