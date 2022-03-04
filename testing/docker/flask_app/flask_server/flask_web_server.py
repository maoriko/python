import flask

app = flask.Flask(__name__)


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
    