import math
nt=[1]*10001
nt[0]=0
nt[1]=0
for i in range(2,int(math.sqrt(10000))+1,1):
    if(nt[i]==1):
        for j in range(i*i,10001,i):
            nt[j]=0
delim=[2,3,5,7]
numTest=int(input())
for i in range(numTest):
    number=input()
    cnt=0
    for i in number:
        if(nt[int(i)]==1):
            cnt+=1
    len_number=len(number)
    if(2*cnt>len_number and nt[len_number]==1):
        print("YES")

    else:
        print("NO")
    
