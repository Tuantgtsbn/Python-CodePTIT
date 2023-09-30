import math
nt=[1]*10001
nt[0]=0
nt[1]=0
for i in range(2,int(math.sqrt(10000))+1,1):
    if(nt[i]==1):
        for j in range(i*i,10001,i):
            nt[j]=0
numTest=int(input())

for i in range(numTest):
    number=input()
    mark=True
    for i in range(len(number)):
        if(not((nt[i]==0 and nt[int(number[i])]==0) or (nt[i]==1 and nt[int(number[i])]==1))):
            mark=False
            break
    if(mark):
        print("YES")
    else:
        print("NO")
