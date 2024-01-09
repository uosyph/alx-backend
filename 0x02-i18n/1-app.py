#!/usr/bin/env python3
"""
Route module for the API.

Endpoints:
    - GET /: Renders the 1-index.html template.
"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

app.url_map.strict_slashes = False


class Config(object):
    """Configuration for language settings."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object("1-app.Config")


@app.route("/", methods=["GET"])
def index() -> str:
    """
    Handle GET requests on the root endpoint.

    Returns:
        Rendered template: 1-index.html
    """
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
