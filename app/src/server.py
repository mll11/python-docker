import flask
from datetime import datetime
import mysql.connector


class DbManager:
    def __init__(self, host='db', database=None, user=None, passwordFilename=None):
        passwordFile = open(passwordFilename, 'r')
        self.connection = mysql.connector.connect(
            user=user,
            password=passwordFile.read(),
            host=host,
            database=database,
            auth_plugin='mysql_native_password'
        )
        passwordFile.close()
        self.cursor = self.connection.cursor()
        self.cursor.execute('DROP TABLE IF EXISTS testdata')
        self.cursor.execute(
            'CREATE TABLE testdata (id INT AUTO_INCREMENT PRIMARY KEY, test_value VARCHAR(255))')
        self.cursor.executemany('INSERT INTO testdata (id, test_value) VALUES (%s, %s);', [
                                (i, 'test #%d' % i) for i in range(1, 4)])
        self.connection.commit()

    def getData(self):
        self.cursor.execute('SELECT test_value FROM testdata')
        valueList = []
        for c in self.cursor:
            valueList.append(c[0])
        return valueList


server = flask.Flask(__name__)
dbConnection = None


@server.route("/")
def home():
    return "Flask Demo"


@server.route("/time")
def time():
    now = datetime.now()
    return now.strftime("%B %d, %Y at %X")


@server.route("/db")
def getDb():
    global dbConnection
    if not dbConnection:
        dbConnection = DbManager(
            database='flask',
            user='root',
            passwordFilename='/run/secrets/secret-mysql-root-password')
    valueList = dbConnection.getData()
    return flask.jsonify({"result": valueList})


if __name__ == "__main__":
    # server.run(host='0.0.0.0')
    # Run server in debug mode.
    server.run(debug=True, host='0.0.0.0')
