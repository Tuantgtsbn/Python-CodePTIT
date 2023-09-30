numTest=int(input())
for i in range(numTest):
    n,d=map(int ,input().split())
    arr=[int(y) for y in input().split()]
    b=arr[d:]+arr[:d]
    for j in b:
        print(j,end=" ")
    print()