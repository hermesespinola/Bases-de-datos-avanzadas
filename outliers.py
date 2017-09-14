from __future__ import division
from matplotlib import pyplot as plt
from math import sqrt, pi, exp, log
import pandas as pd
import numpy as np

def compose(f, g):
    return lambda x: f(g(x))

def gauss(sigma):
    return lambda x: 1 / (sqrt(2 * pi) * sigma) * exp( -x ** 2 / (2 * sigma ** 2) )

def clean(series, apply_log=False):
    sigma = series.std()
    G = series.map(compose(gauss(sigma), log)) if apply_log else series.map(gauss(sigma))
    return G

if __name__ == '__main__':
    data = pd.DataFrame.from_csv("oatmeal.csv").fan_count

    plt.figure(figsize=(12, 6))
    plt.hist(data, bins=100)
    plt.title('Fan count')
    plt.show()

    # See how it looks if we apply logarithm
    data_log = data.map(log)
    plt.figure(figsize=(12, 6))
    plt.hist(data_log, bins=100)
    plt.title('Fan count (logarithm)')
    plt.show()      # It looks much better

    G = clean(data, apply_log=True)
    plt.figure(figsize=(12, 6))
    plt.hist(G, bins=100)
    plt.title('Probability log')
    plt.show()
