from sklearn.linear_model import LinearRegression
import numpy as np

filename = '2004_2009.csv'

puredata = np.loadtxt(filename, delimiter=',')
X = puredata[:, 1:]
Y = puredata[:, 0]

lin=LinearRegression()
lin.fit(X,Y)

y_pred=lin.predict(X)

tes=[]

for i in range(1000):
    print Y[i],y_pred[i],i
    tes.append(Y[i]-y_pred[i])

print np.mean(y_pred)
print np.std(tes,ddof=1)
