from sklearn.svm import SVR
import numpy as np


filename = '2004_2009f.csv'

puredata = np.loadtxt(filename, delimiter=',')
X = puredata[:, 1:]
Y = puredata[:, 0]

svr=SVR()
print "fitting"
svr.fit(X,Y)
print "prediction"
y_pred=svr.predict(X)
list=[]
for i in range(len(X)):
    #print Y[i],y_pred[i],i
    list.append(y_pred[i]-Y[i])

print "Number of tuples: ",len(X)
print "Mean of predictions : ",np.mean(y_pred)
print "Standard deviation : ",np.std(list,ddof=1)
print svr.get_params(deep=True)
