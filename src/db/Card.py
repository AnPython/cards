# -*- coding: utf-8 -*-

from db.db_conn import get_db
from MySQLdb import IntegrityError

class CardManager(object):
    def __init__(self):
        self._conn = get_db()

    def insertCard(self, uid, name, info, phone, email):
        try:
            print "Inserting card"
            cur = self._conn.cursor()
            sql = "INSERT Card(uid, name, info, phone, email)\
                    values(%s, %s, %s, %s, %s)"
            if cur.execute(sql, (uid, name, info, phone, email)) == 1:
                self._conn.commit()
                return True
            return False
        except IntegrityError, e:
            import traceback
            print e
            print traceback.format_exc()
            self._conn.rollback()
            return False

    def updateCard(self, uid, name, info, phone, email):
        try:
            print "Updating card"
            cur = self._conn.cursor()
            sql = "UPDATE Card SET name=%s, info=%s, \
                    phone=%s, email=%s WHERE uid=%s"
            v = cur.execute(sql, (name, info, phone, email, uid))
            if v ==1:
                self._conn.commit()
                return True
            return False
        except IntegrityError, e:
            import traceback
            print e
            print traceback.format_exc()
            self._conn.rollback()
            return False

    def getCardByUid(self, uid):
        try:
            cur = self._conn.cursor()
            sql = "SELECT uid, name, info, phone, email FROM Card \
                    WHERE uid=%s"
            if cur.execute(sql, (uid,)) != 0:
                row = cur.fetchone()
                name = ["uid", "name", "info", "phone", "email"]
                row = dict((name[i], row[i]) for i in range(len(row)))
                return row
            return None
        except IntegrityError, e:
            import traceback
            print e
            print traceback.format_exc()
            self._conn.rollback()
