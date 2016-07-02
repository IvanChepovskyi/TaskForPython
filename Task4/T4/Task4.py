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
for r in sys.argv[1:]:
    rfl=readConsole(r)
    if (posOrneg(rfl)==True):
        print (myPrintPos(rfl))
    else:
        print(myPrintNeg(rfl))