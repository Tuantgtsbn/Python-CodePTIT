numTest=int(input())
for i in range(numTest):
    num=input()
    if(num[:2]==num[-2:]):
        print("YES")
    else:
        print("NO")