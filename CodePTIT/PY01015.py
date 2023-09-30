numTest=int(input())
for i in range(numTest):
    s=input()
    kq=True
    for i in range(len(s)-1):
        if int(s[i])>int(s[i+1]):
            kq=False
            break
    if kq:
        print("YES")
    else:
        print("NO")