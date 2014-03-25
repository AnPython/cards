# -*- coding: utf-8 -*-

import hashlib
import time
import xml.etree.ElementTree as ET

token = "notimetoplay"

text_msg = u"""<xml>
<ToUserName><![CDATA[%s]]></ToUserName>
<FromUserName><![CDATA[%s]]></FromUserName>
<CreateTime>%d</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[%s]]></Content>
</xml>
"""

class Message(object):
    def __init__(self, xml):
        self._raw = xml
        root = ET.fromstring(xml)
        msg = {}
        if root.tag == "xml":
            for node in root:
                msg[node.tag] = node.text
        self.msg = msg

    def get_dict(self):
        return self.msg

    def dump_textmsg(self, content):
        return text_msg % (self.msg["FromUserName"], self.msg["ToUserName"],
                    int(time.time()), content)

def weixin_auth(sign, time, nonce):
    tmplist = [time, nonce, token]
    tmplist.sort()
    hashstr = "".join(tmplist)
    hashstr = hashlib.sha1(hashstr).hexdigest()
    if hashstr == sign:
        return True
    else:
        return False


