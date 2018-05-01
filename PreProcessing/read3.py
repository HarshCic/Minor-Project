import numpy as np

filename = 'dataset.csv'
f1=open('datacheck.csv','wb')

puredata = np.loadtxt(filename, delimiter=',')
X = puredata[:, 1:]
Y = puredata[:, 0]

n=0
sum=0
#grade
for d in X:
    if d[1]!=9:
        sum+=d[1]
        n+=1

gradeavg=int(round(sum/n,0))
print gradeavg

#radseq
n=0
sum=0
for d in X:
    if d[2]!=9:
        sum+=d[2]
        n+=1
radseqavg=int(round(sum/n,0))
print radseqavg

#no of primaries
n=0
sum=0
for d in X:
    if d[3]!=99:
        sum+=d[3]
        n+=1
primariesavg=int(round(sum/n,0))
print primariesavg

#T
n=0
sum=0
for d in X:
    if d[4]!=88:
        sum+=d[4]
        n+=1
tavg=int(round(sum/n,0))
print tavg

#N
n=0
sum=0
for d in X:
    if d[5]!=88:
        sum+=d[5]
        n+=1
navg=int(round(sum/n,0))
print navg

#M
n=0
sum=0
for d in X:
    if d[6]!=88:
        sum+=d[6]
        n+=1
mavg=int(round(sum/n,0))
print mavg

#radiation
n=0
sum=0
for d in X:
    if d[7]!=9:
        sum+=d[7]
        n+=1
radavg=int(round(sum/n,0))
print radavg

#stage
n=0
sum=0
for d in X:
    if d[8]!=99:
        sum+=d[8]
        n+=1
stageavg=int(round(sum/n,0))
print stageavg

#sequence
n=0
sum=0
for d in X:
    if d[11]!=99:
        sum+=d[11]
        n+=1
seqavg=int(round(sum/n,0))
print seqavg

#lymph
n=0
sum=0
for d in X:
    if d[12]!=9:
        sum+=d[12]
        n+=1
lymphavg=int(round(sum/n,0))
print lymphavg

#rx lunsur
n=0
sum=0
for d in X:
    if d[14]!=9:
        sum+=d[14]
        n+=1
rxlunavg=int(round(sum/n,0))
print rxlunavg

#rx summ prime site
n=0
sum=0
for d in X:
    if d[15]!=99:
        sum+=d[15]
        n+=1
rxsummavg=int(round(sum/n,0))
print rxsummavg

#derived ss
n=0
sum=0
for d in X:
    if d[16]!=9:
        sum+=d[16]
        n+=1
derivedssavg=int(round(sum/n,0))
print derivedssavg

#tumour
n=0
sum=0
for d in X:
    if d[17]!=999:
        if d[17]!=888:
            sum+=d[17]
            n+=1
tumouravg=int(round(sum/n,0))
print n
print tumouravg

for d in X:
    if d[1]==9:
        d[1]=gradeavg
    if d[2]==9:
        d[2]=radseqavg
    if d[3]==99:
        d[3]=primariesavg
    if d[4]==88:
        d[4]=tavg
    if d[5]==88:
        d[5]=navg
    if d[6]==88:
        d[6]=mavg
    if d[7]==9:
        d[7]=radavg
    if d[8]==99:
        d[8]=stageavg
    if d[11]==99:
        d[11]=seqavg
    if d[12]==9:
        d[12]=lymphavg
    if d[14]==9:
        d[14]=rxlunavg
    if d[15]==99:
        d[15]=rxsummavg
    if d[16]==9:
        d[16]=derivedssavg
    if d[17]==999:
        d[17]=tumouravg
    if d[17]==888:
        d[17]=tumouravg

for i in range(len(X)):
    f1.write(str(Y[i])+','+str(X[i][0])+','+str(X[i][1])+','+str(X[i][2])+','+str(X[i][3])+','+str(X[i][4])+','+str(X[i][5])+','+str(X[i][6])+','+str(X[i][7])+','+str(X[i][8])+','+str(X[i][9])+','+str(X[i][10])+','+str(X[i][11])+','+str(X[i][12])+','+str(X[i][13])+','+str(X[i][14])+','+str(X[i][15])+','+str(X[i][16])+','+str(X[i][17])+'\n')








