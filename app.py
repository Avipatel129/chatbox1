from flask import Flask, render_template, request

from chat_bot import getInfo

app = Flask(__name__)

@app.get("/")
def index_get():
    return render_template("base.html")

