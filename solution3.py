import math
import operator

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
add=active[:30]
for x in range(1):
    active += add
def normalize(d):
    norm = 0
    for k, v in d.iteritems():
        norm = norm + v ** 2
    norm = math.sqrt(norm)
    for k, v in d.iteritems():
        d[k] = d[k] / norm
    return d
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
    active[i]=getOnlyFeatures(l,1001)
    active[i]=normalize(active[i])
    i+=1
i=0
for l in inactive:
    inactive[i]=getOnlyFeatures(l,1001)
    inactive[i]=normalize(inactive[i])
    i+=1
feature=[]
for x in range(100):
    f={}
    for j in range(len(active)):
        if x in active[j]:
            f[j]=active[j][x]
    for j in range(len(inactive)):
        if x in inactive[j]:
            f[-j-1]=inactive[j][x]
    feature.append(f)
f = open("ans25.dat", "w+")

with open('./test.dat', 'r') as fh:
    lines = fh.readlines()
for l in lines:
    ans=0
    pos_ans = {}
    neg_ans = {}
    l=l.split()
    l=getOnlyFeatures(l,1001)
    l=normalize(l)
    c=0
    for k,v in l.iteritems():

        for j,u in feature[k].iteritems():


            if j >= 0:

                if j in pos_ans:
                    pos_ans[j] += v * u
                else:
                    pos_ans[j] = v*u
            else:
                if j in neg_ans:
                    neg_ans[j] += v * u
                else:
                    neg_ans[j] = v*u
    pos_ans = sorted(pos_ans.items(), key=operator.itemgetter(1))
    pos_ans = pos_ans[-20:]
    neg_ans = sorted(neg_ans.items(), key=operator.itemgetter(1))
    neg_ans = neg_ans[-20:]
    for v in pos_ans:
        ans += v[1]
    for v in neg_ans:
        ans -= v[1]
    if ans >= 0:

        f.write("1\n")
    else:

        f.write("0\n")





