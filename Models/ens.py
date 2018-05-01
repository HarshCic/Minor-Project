from sklearn import ensemble
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
import numpy as np
from sklearn.metrics import mean_squared_error
from math import sqrt

filename = '2004_2009f.csv'

puredata = np.loadtxt(filename, delimiter=',')
X = puredata[:, 1:]
Y = puredata[:, 0]




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





params = {'n_estimators': 500, 'max_depth': 8, 'min_samples_split': 2,
          'learning_rate': 0.001, 'loss': 'ls'}
clf1 = ensemble.GradientBoostingRegressor(**params)

clf2 = DecisionTreeRegressor(max_depth=5)

clf3 = RandomForestRegressor(max_depth=5, random_state=0)

clf4=SVR()

clf1.fit(X,Y)

clf2.fit(X,Y)

clf3.fit(X,Y)

clf4.fit(X,Y)

ypred1=clf1.predict(X)

ypred2=clf2.predict(X)

ypred3=clf3.predict(X)

ypred4=clf4.predict(X)




m, n = np.shape(X)

Y.shape = (m, 1)

x_scale, mean_r, std_r = normalization(X)

# Add a column of ones to X as x0=1
XX = np.ones(shape=(m, 1))
XX = np.append(XX, x_scale, 1)

# set up initial thetas to 0
theta = np.zeros(shape=(n + 1, 1))
# define number of iterations and alpha
iterations = 7000
alpha = 0.001

theta, J_theta_log = gradient_descent(XX, Y, theta, alpha, iterations)
test=0
listd=[]
act=[]
listsd=[]
sumd=0.0
for test in range(len(X)):
    index=test
    f = open('2004_2009f.csv', 'r')
    data=f.readlines()[index-1].split(",")

    temp=[]
    temp.append(1.0)

    for i in range(len(data)-1):
        temp.append((float(data[i+1].split('\n')[0])-mean_r[i])/std_r[i])

    death_rate = np.array(temp).dot(theta)
    listd.append(round(death_rate, 2))
    test+=1
listd=np.array(listd)
"""
print "GBR: ",ypred1[0],len(ypred1)
print "DT: ",ypred2[0],len(ypred2)
print "RF: ",ypred3[0],len(ypred3)
print "SVR",ypred4[0],len(ypred4)
print "linear:",listd[0],len(listd)

print "ensemble:",ypred1[0]*0.62+ypred2[0]*0.096+ypred3[0]*0.057+ypred4[0]*0.158+listd[0]*0.118
"""

final=[]
for i in range(len(X)):
	final.append(ypred1[i]*0.62+ypred2[i]*0.096+ypred3[i]*0.057+ypred4[i]*0.158+listd[i]*0.118)

final=np.array(final)

print "Mean of the predictions : ",np.mean(final)
#print "Standard deviation of residuals: ",np.std(listsd,ddof=1)
print "Standard deviation : ",np.std(final,ddof=1)
#rms=sqrt(mean_squared_error(act,final))
#print "RMSE : ",rms

