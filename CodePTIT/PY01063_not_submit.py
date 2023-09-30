import re
numTest=int(input())
for i in range(numTest):
    numTest=input()
    find_number=input()
    arr=re.findall(find_number,numTest)
    print(len(arr))