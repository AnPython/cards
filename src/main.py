#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from flask import Flask

DEFAULT_APP_NAME = "micro cards"

app=Flask(DEFAULT_APP_NAME)
try:
    app.config.from_object("config_debug.Config")
except:
    app.config.from_object("config.Config")
