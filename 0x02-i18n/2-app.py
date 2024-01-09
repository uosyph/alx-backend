#!/usr/bin/env python3
"""
Route module for the API.

Endpoints:
    - GET /: Renders the 2-index.html template.
"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

app.url_map.strict_slashes = False


class Config(object):
    """Configuration for language settings."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object("2-app.Config")


@app.route("/", methods=["GET"])
def index() -> str:
    """
    Handle GET requests on the root endpoint.

    Returns:
        Rendered template: 2-index.html
    """
    return render_template("2-index.html")


@babel.localeselector
def get_locale() -> str:
    """
    Determine the best-matching supported language based on client preferences.

    Returns:
        str: The best-matching language code from the available languages.
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
