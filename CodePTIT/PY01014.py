a,k,n=[int(x) for x in input().split()]
first=int((a+k-1)/k)*k
last=int(n/k)*k
# print(first,last)
ok=False
if(a%k==0):
    for i in range(first+k,last+1,k):
        ok=True
        print(i-a,end=" ")
else:
    for i in range(first,last+1,k):
        ok=True
        print(i-a,end=" ")
if(ok==False):print(-1)