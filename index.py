from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def helloWorld():
    return "berhasil connect ke db"