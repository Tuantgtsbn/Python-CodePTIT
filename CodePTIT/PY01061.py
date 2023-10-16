from itertools import permutations
import math
nt=[1]*1001
nt[0]=0
nt[1]=0
for i in range(2,int(math.sqrt(1000))+1,1):
    if(nt[i]==1):
        for j in range(i*i,1001,i):
            nt[j]=0

numTest=int(input())
for i in range(numTest):
    number=input()
    arr1=[int(x) for x in number[:3]]
    arr2=[int(x) for x in number[-3:]]
    arr_com1=list(permutations(arr1))
    set_com1=list(set(arr_com1))
    arr_com2=list(permutations(arr2))
    set_com2=list(set(arr_com2))
    kq1=False
    for i in set_com1:
        sum=0
        for j in i:
            sum=sum*10+int(j)
        if(nt[sum]==1):
            kq1=True
            break
    kq2=False
    for i in set_com2:
        sum=0
        for j in i:
            sum=sum*10+int(j)
        if(nt[sum]==1):
            kq2=True
            break
    if(kq1 and kq2):
        print("YES")
    else:
        print("NO")
        

