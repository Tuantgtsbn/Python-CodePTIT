import itertools
s=input()
arr=[x for x in s]
arr=list(itertools.permutations(arr,len(s)))
for i in arr:
    for j in i:
        print(j,end="")
    print()
