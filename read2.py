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

def checksurvival(n):
    if '9999' in n:
        return str(-1)
    else:
        return n

def checkage(age):
    if '999' in age:
        return str(0)
    else:
        return age

def noofprimaries(n):
    if '99' in n:
        return str(0)
    else:
        return n

def checklymph(n):
    if '999' in n:
        return str(0)
    else:
        return n

def checkstage(n):
    if '99' in n:
        return str(0)
    else:
        return n

def checkrxsumm(n):
    if '99' in n:
        return 0
    else:
        return n

def checktumour(n):
    if '999' in n:
        return str(0)
    elif'888' in n:
        return str(0)
    else:
        return n

def checkseq(n):
    if '99' in n:
        return str(0)
    else:
        return n

def checkhistology(n):
    if '98' in n:
        return str(0)
    else:
        return n

f1=open('datamultiple.csv','wb')
f2=open('data2.csv','r')
lines=f2.readlines()[1:]

tmp=0
for x in lines:
    if tmp==8000:
        break
    tmp+=1
    temp=[]
    x=x.split(',')
    temp.append(checksurvival(check(x[107])))
    temp.append(checkage(check(x[6])))
    temp.append(check(x[17]))
    temp.append(check(x[135]))
    temp.append(noofprimaries(check(x[131])))
    temp.append(check(x[128]))
    temp.append(check(x[129]))
    temp.append(check(x[130]))
    temp.append(check(x[133]))
    temp.append(checkstage(check(x[113])))
    temp.append(check(x[11][-1]))
    temp.append(check(x[82]))
    temp.append(checkseq(check(x[8])))
    temp.append(checklymph(check(x[35]))[0])
    temp.append(checkhistology(check(x[71])))
    temp.append(checkrxsumm(check(x[55])))
    temp.append(check(x[54]))
    temp.append(check(x[48]))
    temp.append(checktumour(check(x[20])))
    #temp.append(checksurvival(check(x[107])))
    temp=','.join(temp) + '\n'
    f1.write(temp)



