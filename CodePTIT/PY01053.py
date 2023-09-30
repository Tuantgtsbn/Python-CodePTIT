numTest=int(input())
for i in range(numTest):
    s=input()
    sum=0
    for i in s:
        sum+=int(i)
    if(sum%3):
        print("NO")
    else:
        print("YES")