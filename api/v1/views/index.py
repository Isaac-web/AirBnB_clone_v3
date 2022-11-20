#!/usr/bin/python3
"""Contains routes of app_view blueprints"""

from api.v1.views import app_view
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_view.route("/status")
def status():
    """Returns the status of the app"""
    return jsonify({"status": "OK"})


@app_view.route("/stats")
def get_stats():
    """Statistics of application data"""
    return (jsonify({"amenities": storage.count(Amenity),
                     "cities": storage.count(City),
                     "places": storage.count(Place),
                     "reviews": storage.count(Review),
                     "states": storage.count(State),
                     "users": storage.count(User)}))
