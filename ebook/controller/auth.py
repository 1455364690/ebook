__author__ = 'yangbo'
from functools import wraps
from flask import session, redirect


def requires_auth(fun):
    @wraps(fun)
    def wrapped(*args, **kwargs):
        if "username" in session:
            return fun(*args, **kwargs)
        else:
            return redirect("/")
    return wrapped
