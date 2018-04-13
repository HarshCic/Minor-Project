import numpy as np
from sklearn.ensemble import RandomForestRegressor, VotingClassifier, GradientBoostingRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR


filename = '2004_2009.csv'

puredata = np.loadtxt(filename, delimiter=',')
X = puredata[:, 1:]
Y = puredata[:, 0]


params = {'n_estimators': 500, 'max_depth': 8, 'min_samples_split': 2,
          'learning_rate': 0.001, 'loss': 'ls'}
clf1 = GradientBoostingRegressor(**params)

clf2 = DecisionTreeRegressor(max_depth=5)

clf3 = RandomForestRegressor(max_depth=5, random_state=0)

clf4=SVR()

ens=VotingClassifier(estimators=[('gbr',clf1),('dt',clf2),('rf',clf3),('svr',clf4)],voting='soft')

ens=ens.fit(X,Y)

ypred=ens.predict(X)
ls=[]

for i in range(len(Y)):
    #print ypred[i],Y[i],i
    ls.append(Y[i]-ypred[i])

print "Total tuples: ",len(Y)
print "mean: ",np.mean(ypred)
print "sd: ",np.std(ypred,ddof=1)
