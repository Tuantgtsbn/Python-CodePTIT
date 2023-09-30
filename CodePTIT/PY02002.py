List=[0]*93
List[1]=1
List[2]=1
for i in range(3,93):
    List[i]=List[i-1]+List[i-2]
numTest=int(input())
for i in range(numTest):
    a,b=[int(x) for x in input().split()]
    for i in range(a,b+1):
        print(List[i],end=" ")
    print()