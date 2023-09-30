def value(s):
    sum=0
    for i in range(len(s)):
        sum+=ord(s[i])-ord('A')
    return sum
def rotate(s):
    sum=value(s)
    tmp=""
    for i in range(len(s)):
        tmp+=chr((ord(s[i])-65+sum)%26+65)
    return tmp

def solve(s):
    len_s=len(s)
    s1=s[0:len_s//2]
    s2=s[len_s//2:]
    s1=rotate(s1)
    s2=rotate(s2)
    tmp=""
    for i in range(len(s1)):
        tmp+=chr((ord(s1[i])-65+ord(s2[i])-65)%26+65)
    return tmp


numTest=int(input())
for i in range(numTest):
    s=input()
    print(solve(s))
