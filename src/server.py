#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import getopt

from main import app
from views import oauth, card, weixin, index, mycard
from db import db_conn

try:
    from bae.core.wsgi import WSGIApplication
    application = WSGIApplication(app)
except:
    port = 8080
    app.run(host="0.0.0.0", port=port)
