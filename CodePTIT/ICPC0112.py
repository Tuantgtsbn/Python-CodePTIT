import math
numTest=int(input())
mark=[1]*1000010
mark[0]=mark[1]=0
for i in range(2,int(math.sqrt(1000010)),1):
    if mark[i]==1:
        for j in range(i*i,1000010,i):
            mark[j]=0

for i in range(numTest):
    n=int(input())
    cnt=0
    for i in range(2,n-5,1):
        if(mark[i]==1 and mark[i+2]==1 and mark[i+6]==1):
            cnt+=1
            
        if(mark[i]==1 and mark[i+4]==1 and mark[i+6]==1):
            cnt+=1
            
    print(cnt)
    