from sklearn.tree import DecisionTreeRegressor
import numpy as np
from sklearn.model_selection import train_test_split

filename = '2004_2009f.csv'

puredata = np.loadtxt(filename, delimiter=',')
X = puredata[:, 1:]
Y = puredata[:, 0]

clf = DecisionTreeRegressor(max_depth=5)

clf.fit(X,Y)

ypred=clf.predict(X)
ls=[]

for i in range(len(Y)):
    #print ypred[i],Y[i],i
    ls.append(Y[i]-ypred[i])

print "Total tuples: ",len(Y)
print "mean: ",np.mean(ypred)
print "sd: ",np.std(ypred,ddof=1)
