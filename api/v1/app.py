#!/usr/bin/python3
"""
Contains a flask app
"""
from flask import Flask, make_response, jsonify
from models import storage
from api.v1.view import app_views
import os


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_storage():
    storage.close()


@app.errorhandler(404)
def not_found():
    """
    Not found response
    """
    return make_response(jsonify({"error": "Not found"})), 404


if __name__ == "__main__":
    app.run(host=os.getenv("HBNB_API_HOST", "0.0.0.0"),
            port=os.getenv('HBNB_API_PORT', 5000), threaded=True)
