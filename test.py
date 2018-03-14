"""from sklearn.linear_model import LinearRegression
import numpy as np

filename = '2004_2009.csv'

puredata = np.loadtxt(filename, delimiter=',')
X = puredata[:, 1:]
Y = puredata[:, 0]

lin=LinearRegression()
lin.fit(X,Y)

y_pred=lin.predict(X)

tes=[]

for i in range(100):
    print Y[i],y_pred[i],i
    tes.append(Y[i]-y_pred[i])

print np.mean(y_pred)
print np.std(tes,ddof=1)
"""
"""
age : 7
grade : 18
rediation sequence with surgery : 136
number of primaries : 132
T : 129
N : 130
M : 131
Radiation : 134
stage :114
Primary Site :12
First Malignant Primary Indicator :83
Sequence Number : 9
CS Lymphnodes : 36
Histology Recode-Broad Groupings : 72
RXSumm-ScopeRegLNSur(2003+) :56
RXSumm-SurgPrimSite(1998+) :55
DerivedSS1977 :49
tumour size :21
Survival Time : 108
"""
f1=open('2004_2009.csv','wb')
f2=open('data.csv','r')
lines=f2.readlines()[1:]

tmp=0
for x in lines:
    if tmp==1000:
        break
    tmp+=1
    temp=[]
    x=x.split(',')
    if int(x[10])<2004 or int(x[10])>2009:
        continue
    if int(x[6])==999:
        continue
    if int(x[6])==9:
        continue
    if int(x[135])==9:
        continue
    if int(x[131])==99:
        continue
    if int(x[133])==9:
        continue
    if int(x[47])==99:
        continue
    if int(x[8])==99 | int(x[8])==88:
        continue
    if int(x[35]==999):
        continue
    if int(x[71]==98):
        continue
    if int(x[55])==99:
        continue
    if int(x[54])==9:
        continue
    if int(x[48])==9:
        continue
    if int(x[33])==999 or int(x[3])==888:
        continue
    if int(x[107])==9999:
        continue
    temp.append(x[107])
    temp.append(x[6])
    temp.append(x[17])
    temp.append(x[135])
    temp.append(x[131])
    temp.append(x[128])
    temp.append(x[129])
    temp.append(x[130])
    temp.append(x[133])
    temp.append(x[47])
    temp.append(x[11][1:])
    temp.append(x[82])
    temp.append(x[8])
    temp.append(x[35])
    temp.append(x[71])
    temp.append(x[55])
    temp.append(x[54])
    temp.append(x[48])
    temp.append(x[33])
    temp=','.join(temp) + '\n'
    f1.write(temp)



