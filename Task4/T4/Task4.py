import sys, math
def readConsole(st):
    return float(st)
def posOrneg(fl):
    if fl>0:
        return True
    else:
        return False
def myPrintPos(fl):
    return 'ln('+str(fl)+')= '+str(math.log(fl))
def myPrintNeg(fl):
    return 'ln('+str(fl)+') is illegal'

# first cycle
#for r in sys.argv[1:]:
#    rfl=readConsole(r)
#    if (posOrneg(rfl)==True):
#        print (myPrintPos(rfl))
#    else:
#        print(myPrintNeg(rfl))

#second cycle
#for i in range(1,len(sys.argv)):
#    rfl=readConsole(sys.argv[i])
#    if (posOrneg(rfl)==True):
#        print (myPrintPos(rfl))
#    else:
#        print(myPrintNeg(rfl))

#third cycle
i=1
while i<len(sys.argv):
    rfl=readConsole(sys.argv[i])
    if (posOrneg(rfl)==True):
        print (myPrintPos(rfl))
    else:
        print(myPrintNeg(rfl))
    i=i+1
