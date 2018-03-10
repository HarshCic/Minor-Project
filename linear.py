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

for x in data:
    temp=[]
    for i in range(len(x)):
        if i==18:
            break
        temp.append(float(x[i]))
    dataset.append(temp)

for x in data:
    survival.append(float(x[18]))

for i in range(18):
    maxValues.append(getmax(dataset,i))

print maxValues

for x in dataset:
    for i in range(18):
        x[i]=x[i]/maxValues[i]

print dataset[1]

b=numpy.array(dataset)

print numpy.linalg.inv(b)