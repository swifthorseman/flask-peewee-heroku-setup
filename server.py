from flask import Flask, render_template
from tellytubbies import *

app = Flask(__name__)

@app.route('/')
def index():
    tellytubbies = retrieve_all()
    return render_template("index.html", tellytubbies=tellytubbies)

app.run(debug=True, port=8090, host='0.0.0.0')
