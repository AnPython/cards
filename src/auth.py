#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import session, redirect, url_for, abort, request

def auth(f):
    def auth_f(*args, **keywords):
        if("uid" not in session):
            return redirect(url_for("oauth", referrer=request.url))
        return f(*args, **keywords)
    auth_f.__name__ = f.__name__
    auth_f.__doc__ = f.__doc__
    auth_f.__dict__.update(f.__dict__)
    return auth_f
