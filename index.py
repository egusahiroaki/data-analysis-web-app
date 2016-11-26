#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import time
from flask import Flask, render_template, request, redirect, url_for
import csv
import os
import numpy as np
from matplotlib import pyplot as plt
from scipy import stats
from figure import Figure

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/analysis', methods=['GET', 'POST'])
def analysis():
    file = request.files['file'] 
    csv_lines = []

    for line in file.stream.readlines():
        csv_lines.append(line.decode('utf-8'))

    # if there is no directory, then create
    if not os.path.isdir("csv"):
      os.makedirs("csv")

    # save csv in local directory
    with open('csv/upload.csv', 'w') as f:
      writer = csv.writer(f, lineterminator='\n')
      writer.writerows(csv.reader(csv_lines, delimiter=",", quotechar='"'))

    # analysis
    figure = Figure('csv/upload.csv')
    figure.make()

    return render_template('index.html')

if __name__ == "__main__":
    app.debug = True # デバッグモード有効化
    app.run(host="127.0.0.1", port=5000)
