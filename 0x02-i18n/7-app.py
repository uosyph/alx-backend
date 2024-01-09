#!/usr/bin/env python3
"""
Route module for the API.

Endpoints:
    - GET /: Renders the 7-index.html template.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union
import pytz.exceptions


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)
babel = Babel(app)

app.url_map.strict_slashes = False


class Config(object):
    """Configuration for language settings."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object("7-app.Config")


@app.before_request
def before_request():
    """
    Execute before each request to find and set
    user information in the global Flask context.

    The user information is stored in 'flask.g.user'.
    """
    g.user = get_user()


def get_user() -> Union[dict, None]:
    """
    Retrieve user information based on the 'login_as' query parameter.

    Returns:
        Union[dict, None]: A dictionary containing user information if found,
        otherwise None.
    """
    login_as = request.args.get("login_as")
    if login_as:
        return users.get(int(login_as))
    return None


@app.route("/", methods=["GET"])
def index() -> str:
    """
    Handle GET requests on the root endpoint.

    Returns:
        Rendered template: 7-index.html
    """
    return render_template("7-index.html")


@babel.localeselector
def get_locale() -> str:
    """
    Determine the best-matching supported language based on client preferences.

    Returns:
        str: The best-matching language code from the available languages.
    """
    locale = request.args.get("locale")
    if locale:
        return locale
    elif (
        g.user
        and g.user.get("locale")
        and g.user.get("locale") in app.config["LANGUAGES"]
    ):
        return g.user.get("locale")
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@babel.timezoneselector
def get_timezone() -> Union[str, None]:
    """
    Determine the best-matching supported timezone based on client preferences.

    Returns:
        Union[str, None]: The best-matching timezone code from
        the available timezones if found, otherwise None.

    Raises:
        pytz.exceptions.UnknownTimeZoneError: If an unknown timezone is
        provided in the 'timezone' query parameter or the user's preferences.
    """
    timezone = request.args.get("timezone")
    if timezone:
        try:
            return timezone(timezone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            return None
    elif g.user and g.user.get("timezone"):
        try:
            return timezone(g.user.get("timezone")).zone
        except pytz.exceptions.UnknownTimeZoneError:
            return None
    return app.config["BABEL_DEFAULT_TIMEZONE"]


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
