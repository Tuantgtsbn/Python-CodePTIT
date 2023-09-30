from itertools import permutations
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
    arr=[int(x) for x in number[-4:]]
    arr_com=list(permutations(arr))
    set_com=list(set(arr_com))
    kq=False
    for i in set_com:
        sum=0
        for j in i:
            sum=sum*10+int(j)
        if(nt[sum]==1):
            kq=True
            break
    if(kq):
        print("YES")
    else:
        print("NO")
        

