from itertools import combinations
n,k=[int(x) for x in input().split()]
arr=map(int,input().split())
new_set=set(arr)
new_set_sorted=sorted(list(new_set))
# print(new_set_sorted)
list_com=list(combinations(new_set_sorted,k))
# list_com.sort()
for i in list_com:
    for j in i:
        print(j,end=" ")
    print()
