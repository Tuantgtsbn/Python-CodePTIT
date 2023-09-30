import math
numTest=int(input())
def check_nt(number):
    if(number<2):
        return False
    for i in range(2,int(math.sqrt(number))+1,1):
        if(number%i==0):
            return False
    return True

def check_odd_even(number):
    for i in range(len(number)):
        if(int(number[i])%2!=i%2):
            return False
    return True

for i in range(numTest):
    number=input()
    sum=0
    for i in number:
        sum+=int(i)
    if(check_nt(sum)and check_odd_even(number)):
        print("YES")
    else:
        print("NO")
