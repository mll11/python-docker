from flask import Flask
server = Flask(__name__)


@server.route("/")
def baseUrl():
    return "This is the base url."


if __name__ == "__main__":
    server.run(host='0.0.0.0')
