# from flask import Flask
# 
# app = Flask('app')
# @app.route('/')
# 
# def run():
#     return '<h1>Hello, Server!</h1>'
# 
# app.run(host = '0.0.0.0', port = 8080)


from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


