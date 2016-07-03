import sys
try:
    infilename = sys.argv [1]
    outfilename = sys.argv [2]
except:
    print("Usage : ", sys.argv[0], "infile outfile")
    sys.exit(1)
ifile = open(infilename, 'r')
ofile = open(outfilename,'w')
def myfunc(numb):
    sum=0.0
    for i in range(0,len(numb)):
        sum=sum+numb[i]
    return sum/len(numb)
for line in ifile:
    numbstr = line.split()
    numb=[]
    for i in range(0,len(numbstr)):
        numb.append(float(numbstr[i]))
    middle = myfunc(numb)
    ofile.write('{} {}'.format(numb,middle))
ifile.close()
ofile.close()