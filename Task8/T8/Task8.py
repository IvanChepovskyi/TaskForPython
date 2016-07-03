from random import randint
import sys
n=int(sys.argv[1])
sum=0
for i in range(1,n):
    first=randint(1,6)
    second=randint(1,6)
    third=randint(1,6)
    fourth=randint(1,6)
    if (first==1 or second==1 or third==1 or fourth==1):
        prob=0
    elif (first==2 and second==2 and third==2 and fourth==2):
        prob=0
    else:
        sum=sum+1
prob=sum/n
print('probability of win = ','%6f' % (prob))