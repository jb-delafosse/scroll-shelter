# This module is main to spawn an http server.
#
# In this module, we connect all elements together, in order to make the
# server runnable.

import logging

import app.endpoints.user
from app.infrastructure import web_app

logging.getLogger().setLevel(logging.DEBUG)
web_app.SECRET = "MY SECRET"

APP = web_app.app
