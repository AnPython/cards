# -*- coding: utf-8 -*-

from db.db_conn import get_db

class LibManager(object):
    def __init__(self):
        self._conn = get_db()

    def getCards(self, uid):
        try:
            cur = self._conn.cursor()
            sql = "SELECT tuid, name, info, email, phone \
                    FROM Lib JOIN Card ON \
                    Lib.tuid = Card.uid \
                    WHERE Lib.uid=%s"
            if cur.execute(sql, (uid,)) > 0:
                rows = cur.fetchall()
                result = []
                name = ["uid", "name", "info", "email", "phone"]
                for row in rows:
                    rdict = dict((name[i], row[i]) for i in range(len(row)))
                    result.append(rdict)
                return result
            return None
        except Exception, e:
            import traceback
            print e
            print traceback.format_exc()
            self._conn.rollback()
            return None


    def hasCard(self, uid, tuid):
        try:
            cur = self._conn.cursor()
            sql = "SELECT tuid FROM Lib WHERE uid=%s AND tuid=%s"
            if cur.execute(sql, (uid, tuid)) == 1:
                return True
            return False
        except Exception, e:
            import traceback
            print e
            print traceback.format_exc()
            self._conn.rollback()
            return False

    def addCard(self, uid, tuid):
        try:
            cur = self._conn.cursor()
            sql = "INSERT Lib(uid, tuid) values(%s, %s)"
            if cur.execute(sql, (uid, tuid)) == 1:
                self._conn.commit()
                return True
            return False
        except Exception, e:
            import traceback
            print e
            print traceback.format_exc()
            self._conn.rollback()
            return False

    def deleteCard(self, uid, tuid):
        try:
            cur = self._conn.cursor()
            sql = "DELETE FROM Lib WHERE uid=%s AND tuid=%s"
            v = cur.execute(sql, (uid, tuid))
            if v == 1:
                self._conn.commit()
                return True
            print v
            return False
        except Exception, e:
            import traceback
            print e
            print traceback.format_exc()
            self._conn.rollback()
            return False
