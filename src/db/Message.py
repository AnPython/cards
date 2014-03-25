# -*- coding: utf-8 -*-

try:
    from db.db_conn import get_db
except:
    import MySQLdb
    def get_db():
        return MySQLdb.connect("localhost", "user", "", "cards")

import time

class MessageManager(object):
    def __init__(self):
        self._conn = get_db()

    def insertMessage(self, msg):
        try:
            cur = self._conn.cursor()
            info = msg.get_dict()
            sql = "INSERT Message(ToUserName, FromUserName, CreateTime, \
                    MsgType, Content, MsgId, raw_data) \
                    values(%s, %s, %s, %s, %s, %s, %s)"
            cur.execute(sql, (info["ToUserName"],
                             info["FromUserName"],
                             time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(float(info["CreateTime"]))),
                             info["MsgType"],
                             info["Content"],
                             info["MsgId"],
                             msg._raw))
            self._conn.commit()
            return True
        except:
            self._conn.rollback()
            return False

    def getMessagePage(self, pagenum=1, pagesize=10):
        begin = (pagenum-1) * pagesize
        end = begin + pagesize
        cur = self._conn.cursor()
        cur.execute("SELECT content, created_time FROM Message LIMIT %s, %s", [begin, end])
        return cur.fetchall()
