from flask import Flask
from markupsafe import escape
app = Flask(__name__)

@app.route("/")
def hello():
    return "<p>Hello, World</p>"

@app.route("/<name>")
def dynamic(name):
    return f"Hello, {escape(name)}"