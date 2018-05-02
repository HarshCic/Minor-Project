# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from math import sqrt
from sklearn.cross_validation import train_test_split

filename = '2004_2009f.csv'

puredata = np.loadtxt(filename, delimiter=',')
X = puredata[:, 1:]
Y = puredata[:, 0]

X_train, X_test, Y_train, Y_test=train_test_split(X,Y)

def normalization(x):
    mean_x = []
    std_x = []
    X_normalized = x
    temp = x.shape[1]
    for i in range(temp):
        m = np.mean(x[:, i])
        s = np.std(x[:, i])
        mean_x.append(m)
        if s==0.0:
            s=1.0
        std_x.append(s)
        X_normalized[:, i] = (X_normalized[:, i] - m) / s
    return X_normalized, mean_x, std_x

def cost(x, y, theta):
    m = y.size  # number of training examples
    predicted = np.dot(x, theta)
    sqErr = (predicted - y)
    J = ((1.0) / (2 * m)) * np.dot(sqErr.T, sqErr)
    return J

def gradient_descent(x, y, theta, alpha, iterations):
    m = y.size

    theta_n = theta.size

    J_theta_log = np.zeros(shape=(iterations + 1, 1))

    J_theta_log[0, 0] = cost(x, y, theta)

    for i in range(iterations):


        # split equation in to several parts
        predicted = x.dot(theta)

        for thetas in range(theta_n):
            tmp = x[:, thetas]
            tmp.shape = (m, 1)
            err = (predicted - y) * tmp
            theta[thetas][0] = theta[thetas][0] - alpha * (1.0 / m) * err.sum()
        J_theta_log[i + 1, 0] = cost(x, y, theta)

    return theta, J_theta_log


m, n = np.shape(X_train)

Y_train.shape = (m, 1)

x_scale, mean_r, std_r = normalization(X_train)

# Add a column of ones to X as x0=1
XX = np.ones(shape=(m, 1))
XX = np.append(XX, x_scale, 1)

# set up initial thetas to 0
theta = np.zeros(shape=(n + 1, 1))
# define number of iterations and alpha
iterations = 7000
alpha = 0.001

# calculate theta using gradient descent
theta, J_theta_log = gradient_descent(XX, Y_train, theta, alpha, iterations)
#print(theta)
#print(Y[1, :])
# print(J_log)
#fig = plt.figure('Cost function convergence')
#plt.plot(J_theta_log)
#plt.grid(True)
#plt.xlabel('Iterations')
#plt.ylabel('Cost')
#plt.title('Cost function convergence')
#plt.show()

#test hyphothesis with some values
test = 0
listd = []
act = []
listsd = []
sumd = 0.0
for test in range(len(X_test)):
    index = test
    temp = []
    temp.append(1.0)
    for i in range(len(X_test[test])):
        temp.append((float(X_test[test][i] - mean_r[i]) / std_r[i]))
    death_rate = np.array(temp).dot(theta)
    listd.append(round(death_rate, 2))
    listsd.append(round(Y_test[test]-death_rate,3))
    test += 1
listd = np.array(listd)
print "Mean of the predictions : ",np.mean(listd)
print "Standard deviation of residuals: ",np.std(listsd,ddof=1)
print "Standard deviation : ",np.std(listd,ddof=1)
rms=sqrt(mean_squared_error(Y_test,listd))
print "RMSE : ",rms


#plt.plot(listd,act,'ro')
#plt.grid(True)
#plt.xlabel('Predicted')
#plt.ylabel('Actual')
#plt.show()
