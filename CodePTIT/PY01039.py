numTest=int(input())
for i in range(numTest):
    s=input()
    number1=s[0]
    number2=s[1]
    if(number1==number2):
        print("NO")
    else:
        is_true=all(s[i]==s[i%2] for i in range(2,len(s),1))
        if(is_true):
            print("YES")
        else:
            print("NO")