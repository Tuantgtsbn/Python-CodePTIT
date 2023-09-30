import math


def check_nt(number):

    if (number < 2):
        return False
    for i in range(2, int(math.sqrt(number))+1, 1):
        if (number % i == 0):
            return False
    return True


numTest = int(input())
for i in range(numTest):
    number = input()
    sum = 0

    for i in number:
        sum += int(i)
    # print(sum)
    
    if (check_nt(sum)):
        print("YES")
    else:
        print("NO")
