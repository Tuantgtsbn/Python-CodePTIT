import math
def check(s1):
    s2=s1[::-1]
    for i in range(1,len(s1),1):
        if(int(math.fabs(ord(s1[i])-ord(s1[i-1])))!=int(math.fabs(ord(s2[i])-ord(s2[i-1])))):
            return False
    return True
numTest=int(input())
for i in range(numTest):
    s1=input()
    if(check(s1)):
        print("YES")
    else:
        print("NO")