import numpy as np
from numpy import genfromtxt
data=genfromtxt('datafinal.csv',delimiter=',')

dataset=[]
survival=[]


def normalization(x):
    mean_x = [];
    std_x = [];
    X_normalized = x;
    temp = x.shape[1]
    for i in range(temp):
        m = np.mean(x[:, i])
        s = np.std(x[:, i])
        mean_x.append(m)
        std_x.append(s)
        X_normalized[:, i] = (X_normalized[:, i] - m) / s
    return X_normalized, mean_x, std_x


for x in data:
    temp=[]
    for i in range(len(x)):
        if i==18:
            break
        temp.append(float(x[i]))
    dataset.append(temp)
for x in data:
    survival.append(float(x[18]))

survival=np.array(survival)
dataset=np.array(dataset)
norm,mean,std=normalization(dataset)
print norm[0],'\n',mean[0],'\n',std[0]