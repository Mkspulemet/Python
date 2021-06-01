# -*- coding: utf-8 -*-
"""
Created on Mon May 31 15:55:41 2021

@author: pulemet
"""

from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello() -> str:
    return 'Привет! Пока что это будет Flask!, Django может завтра....'

app.run(host='127.0.0.1', port=8080)
