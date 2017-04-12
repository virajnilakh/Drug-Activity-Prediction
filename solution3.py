import math

with open('./train.dat', 'r') as fh:
    lines = fh.readlines()
active=[]
inactive=[]
for l in lines:
    l=l.split()
    if int(l[0])==0:
        inactive.append(l[1:])
    else:
        active.append(l[1:])
def getOnlyFeatures(list,bucketSize):
    dict = {}
    for w in list:
        if int(w) / bucketSize in dict:
            dict[int(w) / bucketSize] += 1
        else:
            dict[int(w) / bucketSize] = 1
    return dict
i=0
for l in active:
    active[i]=getOnlyFeatures(l,101,i)
    i+=1
i=0
for l in inactive:
    inactive[i]=getOnlyFeatures(l,101,i)
    i+=1
def normalize(d):
    norm = 0
    for k, v in d.iteritems():
        norm = norm + v ** 2
    norm = math.sqrt(norm)
    for k, v in d.iteritems():
        d[k] = d[k] / norm
    return d