with open('./answeka.arff', 'r') as fh:
    lines = fh.readlines()
f = open("answeka.dat", "w+")

for l in lines[16:]:
    l=l.split(",")
    if l[0]=="NO":
        f.write("0\n")
    else:
        f.write("1\n")
f.close()

