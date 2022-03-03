from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# 
# cursor.execute(sql, val)
# 
# web_db.commit()
# 
# print(cursor.rowcount, "record inserted.")


# Show counter on web from connection to mysql DB