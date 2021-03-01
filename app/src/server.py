from flask import Flask
from datetime import datetime

server = Flask(__name__)


@server.route("/")
def home():
    return "Flask Demo"


@server.route("/time")
def time():
    now = datetime.now()
    return now.strftime("%B %d, %Y at %X")


if __name__ == "__main__":
    server.run(host='0.0.0.0')
