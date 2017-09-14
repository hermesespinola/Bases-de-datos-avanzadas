from __future__ import division
from matplotlib import pyplot as plt
from math import sqrt, pi, exp, log
import pandas as pd
import numpy as np

def compose(f, g):
    return lambda x: f(g(x))

def gauss(sigma, mu):
    return lambda x: 1 / (sqrt(2 * pi) * sigma) * exp( -(x - mu) ** 2 / (2 * sigma ** 2) )

def distribution(series, apply_log=False):
    sigma = series.std()
    mu = series.mean()
    G = series.map(compose(gauss(sigma, mu), log)) if apply_log else series.map(gauss(sigma, mu))
    return G

def remove_outliers(data, epsilon):
    prob = compose(gauss(data.std(), data.mean()), log)
    G = data.apply(prob)
    return data[G > epsilon], data[G <= epsilon]

if __name__ == '__main__':
    data = pd.DataFrame.from_csv("oatmeal.csv").fan_count

    plt.figure(figsize=(12, 6))
    plt.hist(data, bins=100)
    plt.title('Fan count')
    plt.show() # It doesn't seems like a normal distribution

    # See how it looks if we apply logarithm
    data_log = data.map(log)
    plt.figure(figsize=(12, 6))
    plt.hist(data_log, bins=100)
    plt.title('Fan count (logarithm)')
    plt.show()

    data_clean, outliers = remove_outliers(data, 7.0066556906595079e-08)
    plt.figure(figsize=(12, 6))
    plt.hist(data_clean, bins=100)
    plt.title('Data clean')
    plt.show()

    plt.figure(figsize=(12, 6))
    plt.hist(outliers, bins=100)
    plt.title('Outliers')
    plt.show()
