import math
numTest=int(input())
def checknt(n):
    if n<2:return False
    elif n==2:return True
    else:
        for i in range(2,int(math.sqrt(n))+1,1):
            if(n%i==0):return False
        return True
def gcd(a,b):
    if(b==0):return a
    else: return gcd(b,a%b)
for i in range(numTest):
    a,b=[int(x) for x in input().split()]
    x=gcd(a,b)
    sum=0
    while(x!=0):
        sum+=x%10
        x//=10
    if(checknt(sum)):print("YES")
    else:print("NO")
