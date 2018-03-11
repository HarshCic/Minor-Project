import numpy
from numpy import genfromtxt
data=genfromtxt('datafinal.csv',delimiter=',')

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
        if i==18:
            break
        temp.append(float(x[i]))
    dataset.append(temp)

print len(dataset)
tmp=0
for x in data:
    if tmp==8000:
        break
    tmp+=1
    survival.append(float(x[18]))

maxsurvival=max(survival)

for i in range(len(survival)):
    survival[i]=survival[i]/maxsurvival

for i in range(19):
    maxValues.append(getmax(dataset,i))

for x in dataset:
    for i in range(19):
        x[i]=x[i]/maxValues[i]

print dataset[0]

y=numpy.array(survival)
a=numpy.array(dataset)
"""
transpose=a.transpose()

b=numpy.matmul(transpose,a)

c=numpy.linalg.inv(b)

d=numpy.matmul(c,transpose)

theta=numpy.matmul(d,y)
"""
theta=numpy.linalg.inv(a.T.dot(a)).dot(a.T).dot(y)
print maxValues

print theta
for j in range(10):
    ans=0.0
    for i in range(len(theta)):
        ans=ans+theta[i]*(dataset[j][i]/maxValues[i])
    print ans*maxsurvival,survival[j]*maxsurvival

print maxsurvival