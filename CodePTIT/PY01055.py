numTest=int(input())
def check1(number):
    if len(number)%2==0:
        return False
    else:
        return True
def check2(number):
    if(number[0]!=number[1]):
        return True
    return False
def check3(number):
    for i in range(2,len(number),2):
        if(number[i]!=number[0]):
            return False
    return True
for i in range(numTest):
    number=input()
    # print(len(number))
    if(check1(number) and check2(number) and check3(number)):
        print("YES")
    else:
        print("NO")