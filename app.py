from flask import Flask, make_response

app = Flask(__name__)


@app.route("/")
def hello_world():
    res = make_response("<b>Hello world</b>")
    res.status_code = 200
    return res
