numTest=int(input())
for i in range(numTest):
    s=input()
    result=""
    for i in range(len(s)):
        if s[i].isalpha():
            repeat=int(s[i+1])
            result=result+s[i]*repeat
            i+=2
    print(result)
    