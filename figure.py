# -*- coding: utf-8 -*-

# matplotlibにより図を作成するクラス
import numpy as np
from matplotlib import pyplot as plt
from scipy import stats

class Figure:
    def __init__(self, csv_path):
        '''
        ローカルのcsvファイルパスで初期化
        '''
        self.__csv_data = np.genfromtxt(csv_path, delimiter=",", names=True, dtype=np.uint8)

    def make(self):
        '''
        図を作成する。
        '''
        column_names = self.__csv_data.dtype.names # get header column name

        # this conversion may be not needed.
        data = np.array(self.__csv_data.tolist())
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
        plt.close("all")

