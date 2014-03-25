# -*- coding: utf-8 -*-


from main import app

ak = app.config["MYSQL_USERNAME"]
sk = app.config["MYSQL_PASSWORD"]

def writelog(log):
    try:
        import logging
        from bae_log import handlers
        handler = handlers.BaeLogHandler(ak=ak, sk=sk, bufcount=1)
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        logger.addHandler(handler)
        logger.debug(log)
    except ImportError:
        print "Log: %s" % log
