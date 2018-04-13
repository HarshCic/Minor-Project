"""
-age : 7
-grade : 18
rediation sequence with surgery : 136
number of primaries : 132
T : 129
N : 130
M : 131
Radiation : 134
stage :48
-Primary Site :12
First Malignant Primary Indicator :83
-Sequence Number : 9
CS Lymphnodes : 36
Histology Recode-Broad Groupings : 72
RXSumm-ScopeRegLNSur(2003+) :56
RXSumm-SurgPrimSite(1998+) :55
DerivedSS1977 :49
-tumour size :34
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
        return str(0)
    else:
        return n

def checkrxlunsur(n):
    if '9' in n:
        return str(0)
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
    elif '88' in n:
        return str(0)
    else:
        return n

def checkhistology(n):
    if '98' in n:
        return str(0)
    else:
        return n

def checkgrade(n):
    if '9' in n:
        return str(0)
    else:
        return n

def checkradseq(n):
    if '9' in n:
        return str(0)
    else:
        return n

def checkrad(n):
    if '9' in n:
        return str(0)
    else:
        return n

def checkderivedss(n):
    if '9' in n:
        return str(0)
    else:
        return n

f1=open('2004_2009f.csv','wb')

#f1.write('age,grade,rediation sequence with surgery,number of primaries,T,N,M,Radiation,stage,Primary Site'+
#         'First Malignant Primary Indicator,Sequence Number,CS Lymphnodes,Histology Recode-Broad Groupings'+
#         'RXSumm-ScopeRegLNSur(2003+),RXSumm-SurgPrimSite(1998+),DerivedSS1977,tumour size,Survival Time'+'\n')

f2=open('data.csv','r')
lines=f2.readlines()[1:]

tmp=0
for x in lines:
    #if tmp==1000:
    #    break
    temp=[]
    x=x.split(',')
    if int(x[10])<2004 or int(x[10])>2009:
        continue
    if int(x[107])>72:
        continue
    temp.append(checksurvival(check(x[107])))
    temp.append(checkage(check(x[6])))
    temp.append(checkgrade(check(x[17])))
    temp.append(checkradseq(check(x[135])))
    temp.append(noofprimaries(check(x[131])))
    temp.append(check(x[44]))
    temp.append(check(x[45]))
    temp.append(check(x[46]))
    temp.append(checkrad(check(x[133])))
    temp.append(checkstage(check(x[47])))
    temp.append(check(x[11][-1]))
    temp.append(check(x[82]))
    temp.append(checkseq(check(x[8])))
    temp.append(checklymph(check(x[35]))[0])
    temp.append(checkhistology(check(x[71])))
    temp.append(checkrxlunsur(check(x[55])))
    temp.append(checkrxsumm(check(x[54])))
    temp.append(checkderivedss(check(x[48])))
    temp.append(checktumour(check(x[33])))
    #temp.append(checksurvival(check(x[107])))
    temp=','.join(temp) + '\n'
    f1.write(temp)
    tmp+=1
