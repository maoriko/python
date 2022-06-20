import flask
import logging
import os

app = flask.Flask(__name__)

home = os.environ['HOME']
print("HOME:", home)


@app.route("/")
def general():
    return "200"


@app.route("/hello")
def hello():
    return "Hello World!"


@app.route("/my_ip")
def index():
    ip_address = flask.request.remote_addr
    return "Requester IP: " + ip_address


@app.route("/health")
def health():
    return "service is healthy"


# ConfigMap
# @app.route("/hey")
# def hey():
#     app.config.from_pyfile('/config/config.cfg')
#     return app.config['MSG']


@app.route("/dodo")
def hey():
    app.config.from_pyfile('/config/config.cfg')
    return app.config['DONT']


# Log file
logging.basicConfig(filename='/var/log/record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')


@app.route('/blogs')
def blog():
    app.logger.info('Info level log')
    app.logger.warning('Warning level log')
    return f"Welcome to the Blog"


app.run(host='localhost', debug=True)