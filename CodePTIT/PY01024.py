import math
numTest=int(input())

def is_odd_even(number):
    check2=True
    
    after_number=int(number%10)
    sum_number=after_number
    before_number=0
    number//=10
    while(number>0):
        before_number=int(number%10)
        
        number//=10
        if(math.fabs(before_number-after_number)!=2):
            check2=False
            break
        sum_number+=before_number
        after_number=before_number
        number//10
    # print(sum_number)
    if check2 and (sum_number%10==0):
        print("YES")
    else:
        print("NO")

for i in range(numTest):
    number=int(input())
    is_odd_even(number)
