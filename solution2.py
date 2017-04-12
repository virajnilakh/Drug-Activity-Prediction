from sklearn import svm
with open('./train.dat', 'r') as fh:
    lines = fh.readlines()
compounds=[]
labels=[]
i=0
for l in lines:
    l = l.split()
    compounds.append(l)
    labels.append(compounds[i][0])
    compounds[i]=compounds[i][1:]
    i+=1
clf=svm.SVC()
clf.fit(compounds,labels)
f = open("ans1.dat", "w+")

with open('./test.dat', 'r') as fh:
    lines = fh.readlines()
for l in lines:
    f.write(clf.predict(l))