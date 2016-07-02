import sys, random
def compute (n):
    i = 0 
    s = 0
    while i <= n:
        s += random.random()
        i += 1
    return s/n
n = int(sys.argv [1],10)
print ("average of",n, "random numbers is ","%g" % compute (n))