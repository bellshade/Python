# Daftar package yang kita pakai
from flask import Flask

# Create an instance of Flask
app = Flask(__name__)

# API resource routes
@app.route('/costumeurl/', methods=['GET', 'POST'])
def costumeurl():
    return "Selamat Kamu Berhasil, Lanjutkan Tutuorialnya"

# Api running di localhost dengan port 2020
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=2020)