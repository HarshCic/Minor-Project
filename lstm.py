import numpy
import matplotlib.pyplot as plt
from pandas import read_csv
import math
from keras.models import Sequential
from keras.layers import Dense, LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error

filename = '2004_2009.csv'

puredata = numpy.loadtxt(filename, delimiter=',')
X = puredata[:, 1:]
Y = puredata[:, 0]

scalar=MinMaxScaler(feature_range=(0,1))

d