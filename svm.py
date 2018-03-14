from sklearn.svm import SVR
import numpy as np

filename = '2004_2009.csv'

puredata = np.loadtxt(filename, delimiter=',')
X = puredata[:, 1:]
Y = puredata[:, 0]

svr=SVR(kernel='poly',C=1e3,degree=5)
svr.fit(X,Y)

y_pred=svr.predict(X)

for i in range(50):
    print Y[i],y_pred[i]
