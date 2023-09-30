numTest=int(input())
def gcd(number1,number2):
    if(number2==0):
        return number1
    else:
        return gcd(number2,number1%number2)
def is_true(number):
    number_to_string=str(number)
    number_reverse=int(number_to_string[::-1])
    # print(number_reverse)
    if(gcd(number,number_reverse)==1):
        print("YES")
    else:
        print("NO")
for i in range(numTest):
    number=int(input())
    is_true(number)
