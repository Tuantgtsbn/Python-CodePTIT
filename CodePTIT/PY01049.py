import math
numTest=int(input())
def is_prinme(number):
    if(number<2):
        return False
    for i in range(2,int(math.sqrt(number))+1,1):
        if(number%i==0):
            return False
    return True
for i in range(numTest):
    number=input()
    number_prime=0
    number_not_prime=0
    number_to_string=str(number)
    for i in number_to_string:
        if(is_prinme(int(i))==True):
            number_prime+=1
        else:
            number_not_prime+=1
    if((number_prime>number_not_prime) and is_prinme(len(number_to_string))==True):
        print("YES")
    else:
        print("NO")
