from __future__ import division
from math import exp,log

with open('./train.dat', 'r') as fh:
    lines = fh.readlines()
max=0
min=100
compounds=[]
labels=[]
i=0
for l in lines:
    l = l.split()
    compounds.append(l)
    labels.append(compounds[i][0])
    compounds[i]=compounds[i][1:]
    i+=1
for l in compounds:
    for w in l:
        if max<int(w):
            max=int(w)
        if min>int(w):
            min=int(w)
p1={}
p0={}
pzero=0
pone=0
p1c=0
p0c=0
def getFeatureSets(list,bucketSize,i):
    dict={}
    global p1,p0,pone,pzero,p1c,p0c
    if(int(labels[i])):
        pone+=1
        p1c+=len(list)
        for w in list:
            if int(w)/bucketSize in p1:
                p1[int(w)/bucketSize]+=1
            else:
                p1[int(w)/bucketSize]=1
            if int(w)/bucketSize in dict:
                dict[int(w)/bucketSize]+=1
            else:
                dict[int(w)/bucketSize]=1
    else:
        pzero+=1
        p0c+=len(list)
        for w in list:
            if int(w)/bucketSize in p0:
                p0[int(w)/bucketSize]+=1
            else:
                p0[int(w)/bucketSize]=1
            if int(w)/bucketSize in dict:
                dict[int(w)/bucketSize]+=1
            else:
                dict[int(w)/bucketSize]=1


    return dict
def getOnlyFeatures(list,bucketSize):
    dict = {}
    for w in list:
        if int(w) / bucketSize in dict:
            dict[int(w) / bucketSize] += 1
        else:
            dict[int(w) / bucketSize] = 1
    return dict
i=0
for l in compounds:
    compounds[i]=getFeatureSets(l,101,i)
    i+=1
f = open("ans1.dat", "w+")

with open('./test.dat', 'r') as fh:
    lines = fh.readlines()
p1c*=21
t=p1c+p0c
i=0
j=0
for l in lines:
    l=l.split()
    prob1=0
    prob0=0
    l=getOnlyFeatures(l,101)
    for k,v in l.iteritems():

        if k in p1:
            prob1+=log((p1[k]*21+1)/(p1c+t))
        else:
            prob1+=log((0+1)/(p1c+t))
        if prob1==0:
            print "prob1 j is %d and i is %d"%(j,i)
        if k in p0:
            prob0+=log((p0[k]+1)/(p0c+t))
        else:
            prob0+=log((0+1)/(p0c+t))
        j+=1
        if prob0==0:
            print "prob 2 j is %d and i is %d"%(j,i)
    prob1+=log(pone*21)
    prob0+=log(pzero)
    if prob1>prob0:
        f.write("1\n")
    else:
        f.write("0\n")
    i+=1



