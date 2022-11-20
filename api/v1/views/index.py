#!/usr/bin/python3
"""
Comment here ...
"""
from api.v1.views import app_views
from flask import jsonify


@app_view.route("/status")
def status():
    """
    returns the status
    """
    return jsonify({"status": "OK"})
