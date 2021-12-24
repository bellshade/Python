# Daftar package yang kita pakai
from flask import Flask, request


# Create an instance of Flask
app = Flask(__name__)


# API resource routes
@app.route("/method", methods=["POST", "GET"])
def handle_person():
    if request.method == "POST":
        return "Kamu mengirim menggunakan POST method"
    else:
        return "Kamu mengirim menggunakan GET method"


# Api running di localhost dengan port 2020
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=2020)
