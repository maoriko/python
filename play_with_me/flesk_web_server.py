from flask import Flask
import mysql.connector

print("hi")

config = {
    'user': 'root',
    'password': 'root',
    'host': '127.0.0.1',
    'database': 'web_db',
    'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)

cnx.close()

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"



