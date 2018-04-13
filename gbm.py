from sklearn import ensemble
import numpy as np

filename = '2004_2009.csv'

puredata = np.loadtxt(filename, delimiter=',')
X = puredata[:, 1:]
Y = puredata[:, 0]


params = {'n_estimators': 500, 'max_depth': 8, 'min_samples_split': 2,
          'learning_rate': 0.001, 'loss': 'ls'}
clf = ensemble.GradientBoostingRegressor(**params)

clf.fit(X,Y)

ypred=clf.predict(X)
ls=[]

for i in range(len(Y)):
    #print ypred[i],Y[i],i
    ls.append(Y[i]-ypred[i])

print "Total tuples: ",len(Y)
print "mean: ",np.mean(ypred)
print "sd: ",np.std(ypred,ddof=1)
