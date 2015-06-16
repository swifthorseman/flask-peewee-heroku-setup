from flask import Flask, render_template, g
from tellytubbies import retrieve_all, db_proxy

app = Flask(__name__)

@app.before_request
def before_request():
    g.db = db_proxy
    g.db.connect()

@app.after_request
def after_request(response):
    g.db.close()
    return response

@app.route('/')
def index():
    tellytubbies = retrieve_all()
    return render_template("index.html", tellytubbies=tellytubbies)

