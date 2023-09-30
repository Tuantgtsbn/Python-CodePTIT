import re
numTest=int(input())
for i in range(numTest):

    number=input()

    if(re.search('[^47]',number)):
        print("NO")
    else:
        print("YES")
