from sklearn.svm import SVR
import numpy as np

filename = '2004_2009.csv'

puredata = np.loadtxt(filename, delimiter=',')
X = puredata[:, 1:]
Y = puredata[:, 0]

svr=SVR(kernel='poly',C=0.001,degree=3)
print "fitting"
svr.fit(X,Y)
print "prediction"
y_pred=svr.predict(X)
list=[]
for i in range(50):
    print Y[i],y_pred[i],i
    list.append(y_pred[i]-Y[i])

print "Mean of predictions : ",np.mean(y_pred)
print "Standard deviation : ",np.std(list,ddof=1)
