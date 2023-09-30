import math
numTest=int(input())
def check(number):
    s=str(number)
    tmp=s[::-1]
    if(s==tmp):
        for i in range(len(s)):
            if(int(s[i])%2):
                return False
        return True
    return False

for test in range(numTest):
    number=int(input())
    lennumber=len(str(number))
    for i in range(2,lennumber+1,2):
        if(int(math.pow(10,i))<number):
            for j in range(int(math.pow(10,i-1)),int(math.pow(10,i))):
                if(check(j)):
                    print(j,end=" ")
        else:
            for j in range(int(math.pow(10,i-1)),number):
                if(check(j)):
                    print(j,end=" ")
    print(end="\n")
    