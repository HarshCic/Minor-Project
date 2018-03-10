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

def check(name):
    if ' ' in name:
        return str(0)
    else:
        return name

f1=open('datafinal.csv','wb')
f2=open('data2.csv','r')
lines=f2.readlines()[1:]

for x in lines:
    temp=[]
    x=x.split(',')
    temp.append(check(x[6]))
    temp.append(check(x[17]))
    temp.append(check(x[135]))
    temp.append(check(x[131]))
    temp.append(check(x[128]))
    temp.append(check(x[129]))
    temp.append(check(x[130]))
    temp.append(check(x[133]))
    temp.append(check(x[113]))
    temp.append(check(x[11][-1]))
    temp.append(check(x[82]))
    temp.append(check(x[8]))
    temp.append(check(x[35]))
    temp.append(check(x[71]))
    temp.append(check(x[55]))
    temp.append(check(x[54]))
    temp.append(check(x[48]))
    temp.append(check(x[20]))
    temp.append(check(x[107]))
    temp=','.join(temp) + '\n'
    f1.write(temp)



