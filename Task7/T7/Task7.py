from random import randint
import sys
n=int(sys.argv[1])
sum=0
for i in range(1,n):
    first=randint(1,6)
    second=randint(1,6)
    if (first==6):
        sum=sum+1
    elif (second==6):
        sum=sum+1
prob=sum/n
print('probability of 6 = ','%6f' % (prob))

