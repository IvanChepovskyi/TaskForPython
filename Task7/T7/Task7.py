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
prob=round(prob,3)
left=n*prob-1+prob
right=n*prob+prob
print('the most probable number of tests = ')
for i in range(int(left),int(right)):
    print(i)

