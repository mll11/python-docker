import flask
from datetime import datetime

app = flask.Flask(__name__)


@app.route("/")
def home():
    return "Flask Demo"


@app.route("/time")
def time():
    now = datetime.now()
    return now.strftime("%B %d, %Y at %X")
    # return now.strftime("%A, %d %B, %Y at %X")
    # return now.strftime("%a, %d %B, %Y at %X")
    # return now.strftime("%a, %d %b, %Y at %X")
    # return now.strftime("%a, %d %b, %y at %X")
