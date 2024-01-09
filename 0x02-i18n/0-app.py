#!/usr/bin/env python3
"""
Route module for the API.

Endpoints:
    - GET /: Renders the 0-index.html template.
"""

from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/", methods=["GET"])
def index():
    """
    Handle GET requests on the root endpoint.

    Returns:
        Rendered template: 0-index.html
    """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
