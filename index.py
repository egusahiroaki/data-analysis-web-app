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
    csv_data = np.genfromtxt('csv/upload.csv', delimiter=",", names=True, dtype=np.uint8)
    column_names = csv_data.dtype.names # get header column name

    # this conversion may be not needed.
    data = np.array(csv_data.tolist())
    x = data[:, 0] # get 0 row
    y = data[:, 1]

    plt.rc('font', **{'family': 'serif'})
    fig = plt.figure()
    ax = fig.add_subplot(111)

    slope, intercept, r, _, _ = stats.linregress(x, y)

    print("slope: ", slope)
    print("intercept: ", intercept)
    print("r: ", r)

    plt.xlabel(column_names[0]) # x 
    plt.ylabel(column_names[1]) # y 
    sc = ax.scatter(x, y, s=25, marker='x', color='b')
    plt.plot(x, x*slope + intercept)
    # グリッド表示
    ax.grid(True)
    local_path = "fig.png"
    plt.savefig(local_path)
    plt.show()
    plt.close("all")

    return render_template('index.html')

if __name__ == "__main__":
    app.debug = True # デバッグモード有効化
    app.run(host="127.0.0.1", port=5000)
