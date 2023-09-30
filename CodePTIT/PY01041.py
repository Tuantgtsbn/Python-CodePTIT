numTest=int(input())
def check(s):
    if(len(s)<3):
        return False
    else:
        index=0
        for i in range(1,len(s)):
            if(int(s[index])<int(s[i])):
                index=i
            else:
                break
        if(index==0 or index==len(s)-1):
            return False
        else:
            for j in range(index+1,len(s)):
                if(s[j]>=s[j-1]):
                    return False
            return True
for i in range(numTest):
    s=input()
    if(check(s)):
        print("YES")
    else:
        print("NO")
