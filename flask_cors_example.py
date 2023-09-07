#exec(__import__("requests").get("https://raw.githubusercontent.com/ForkInABlender/ChatGPT_solutions_produced_from_simple_prompt/2023_04/load_anywhere_flask_app.py").text)

#Dylan Kenneth Eliot
"""
I tested this a while back. Most of it was to test out how to make an application that lets CORS not get CORB'ed.

At any rate, this should allow for multiple resources from multiple origins for use in your web apps.

"""

from flask import Flask
from flask_cors import CORS, cross_origin
from requests import get

app = Flask(__name__)
CORS(app)
@app.route("/*", methods=["OPTIONS"]) # needs to be set for { "OPTIONS * HTTP/1.1" 200 -} in output console/log-file...
def star_OPTIONS():
	return "", 200
@app.route("/", methods=["GET"])
@cross_origin()
def index():
    return get("https://raw.githubusercontent.com/ForkInABlender/ChatGPT_solutions_produced_from_simple_prompt/2023_04/test_index.html").text
app.run(host="0.0.0.0")
