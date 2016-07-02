import sys, math
try :
    outfilename = sys.argv[1]
except :
    print("Usage: ",sys.argv[0]," outfile ")
    sys.exit(1)
ofile = open(outfilename, 'w')
def myfunc(y):
    if (y>=0.0):
        return y**5*math.exp(-y)
    else:
        return 0.0
if(len(sys.argv)%2==0):
    for i in range(2,len(sys.argv)):
        if (i%2==0):
            x = float(sys.argv[i])
        else:
            y = float(sys.argv[i])
            fy = myfunc(y)
            ofile.write('%g %12.5e\n' % (x, fy))
else:
    print("Please, write pairs of numbers!")
ofile.close()