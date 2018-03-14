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
f1=open('2004_2009.csv','wb')

f1.write('Survival Time,age,grade,rediation sequence with surgery,number of primaries,T,N,M,Radiation,stage,Primary Site,'+
         'First Malignant Primary Indicator,Sequence Number,CS Lymphnodes,Histology Recode-Broad Groupings,'+
         'RXSumm-ScopeRegLNSur(2003+),RXSumm-SurgPrimSite(1998+),DerivedSS1977,tumour size'+'\n')

f2=open('data.csv','r')
lines=f2.readlines()[1:]

tmp=0
for x in lines:
    #if tmp==10000:
        #break
    tmp+=1
    temp=[]
    x=x.split(',')
    if int(x[10])<2004 or int(x[10])>2009:
        continue
<<<<<<< HEAD
    if int(x[107])>72:
        continue
    temp.append(checksurvival(check(x[107])))
    temp.append(checkage(check(x[6])))
    temp.append(checkgrade(check(x[17])))
    temp.append(checkradseq(check(x[135])))
    temp.append(noofprimaries(check(x[131])))
    temp.append(check(x[128]))
    temp.append(check(x[129]))
    temp.append(check(x[130]))
    temp.append(checkrad(check(x[133])))
    temp.append(checkstage(check(x[47])))
    temp.append(check(x[11][-1]))
    temp.append(check(x[82]))
    temp.append(checkseq(check(x[8])))
    temp.append(checklymph(check(x[35]))[0])
    temp.append(checkhistology(check(x[71])))
    temp.append(checkrxsumm(check(x[55])))
    temp.append(checkrxlunsur(check(x[54])))
    temp.append(checkderivedss(check(x[48])))
    temp.append(checktumour(check(x[33])))
    #temp.append(checksurvival(check(x[107])))
=======
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
>>>>>>> dfcde0abf9569a178b0f51d57ecbdb09a550429a
    temp=','.join(temp) + '\n'
    f1.write(temp)



