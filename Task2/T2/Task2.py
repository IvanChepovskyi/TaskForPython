#import sys
from random import uniform
#if len(sys.argv)>1:
#    n=sys.argv[1]
#else:
#    n=0
n=10
i=0
sum=0.0
while i!=n:
    a=uniform(-1,1)
    sum=sum+a
    print ("%.4f" % (a))
    i=i+1
middle=sum/n
print("middle = ","%.4f" % (middle))