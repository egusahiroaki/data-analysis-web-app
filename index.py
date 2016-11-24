#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import time
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    print('on index')
    app.run(host="127.0.0.1", port=5000)
