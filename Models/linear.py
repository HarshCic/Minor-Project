"""
import numpy
from numpy import genfromtxt
data=genfromtxt('datamultiple.csv',delimiter=',')

dataset=[]
survival=[]
maxValues=[]

def getmax(dataset,index):
    temp=[]
    for x in dataset:
        temp.append(x[index])
    return max(temp)

tmp=0
for x in data:
    if tmp==8000:
        break
    tmp+=1
    temp=[]
    temp.append(int(1))
    for i in range(len(x)):
        if i==0:
            continue
        temp.append(float(x[i]))
    dataset.append(temp)

#print len(dataset)
tmp=0
for x in data:
    if tmp==8000:
        break
    tmp+=1
    survival.append(float(x[0]))

maxsurvival=max(survival)

for i in range(len(survival)):
    survival[i]=survival[i]/maxsurvival

for i in range(19):
    maxValues.append(getmax(dataset,i))

for x in dataset:
    for i in range(19):
        x[i]=x[i]/maxValues[i]

#print dataset[0]

y=numpy.array(survival)
a=numpy.array(dataset)

transpose=a.transpose()

b=numpy.matmul(transpose,a)

c=numpy.linalg.inv(b)

d=numpy.matmul(c,transpose)

theta=numpy.matmul(d,y)

theta=numpy.linalg.inv(a.T.dot(a)).dot(a.T).dot(y)
#print maxValues

#print theta
for j in range(10):
    ans=0.0
    for i in range(len(theta)):
        ans=ans+theta[i]*(dataset[j][i]/maxValues[i])
    print ans*maxsurvival,survival[j]*maxsurvival

print maxsurvival
"""

# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

filename = 'datamultiple.csv'

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
        std_x.append(s)
        X_normalized[:, i] = (X_normalized[:, i] - m) / s
    return X_normalized, mean_x, std_x

m, n = np.shape(X)

Y.shape = (m, 1)

x_scale, mean_r, std_r = normalization(X)

# Add a column of ones to X as x0=1
XX = np.ones(shape=(m, 1))
XX = np.append(XX, x_scale, 1)

theta=np.linalg.inv(XX.T.dot(XX)).dot(XX.T).dot(Y)


test=0
listd=[]
while test !=20:
    #index=int(raw_input("give index value: "))
    #test=index
    index=test
    f = open('datamultiple.csv', 'r')
    data=f.readlines()[index-1].split(",")

    #print data,len(data)
    temp=[]
    temp.append(1.0)

    for i in range(len(data)-1):
        temp.append((float(data[i+1].split('\n')[0])-mean_r[i])/std_r[i])

    death_rate = np.array(temp).dot(theta)
    listd.append(round(death_rate,2))
    print round(death_rate,2),Y[test]

    #print len(mean_r), len(std_r)
    test+=1
listd=np.array(listd)
print "Mean of the predictions : ",np.mean(listd)
print "Standard deviation : ",np.std(listd)
