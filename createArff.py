with open('./train.dat', 'r') as fh:
    lines = fh.readlines()
max = 0
min = 100
compounds = []
labels = []
i = 0
for l in lines:
    l = l.split()


    # labels.append("?")
    if int(l[0]) == 1:
        for k in xrange(10):
            compounds.append(l)
            labels.append(compounds[i][0])
            compounds[i] = compounds[i][1:]
            i += 1
    else:
        compounds.append(l)
        labels.append(compounds[i][0])
        compounds[i] = compounds[i][1:]
        i += 1

for l in compounds:
    for w in l:
        if max < int(w):
            max = int(w)
        if min > int(w):
            min = int(w)


def getFeatureSets(list, dict, bucketSize):
    for w in list:
        dict[int(w) / bucketSize] += 1

    return dict


i = 0
f = open("weka.arff", "w+")
f.write("@RELATION Drug_Activity \n")
f.write("@ATTRIBUTE active {YES,NO} \n")


def createArff(list, bucketSize, f):
    i = 0
    dict = {}
    for x in xrange(max / bucketSize + 1):
        f.write("@ATTRIBUTE feature%d NUMERIC \n" % x)
    f.write("@DATA \n")
    for l in list:
        for x in xrange(max / bucketSize + 1):
            dict[x] = 0
        compounds[i] = getFeatureSets(l, dict, bucketSize)
        if (int(labels[i]) == 1):
            f.write("YES")
        else:
            f.write("NO")
        # f.write(labels[i])
        for k, v in compounds[i].iteritems():
            f.write("," + str(v));
        f.write("\n")
        i += 1
    pass


createArff(compounds, 10000, f)
f.close()


