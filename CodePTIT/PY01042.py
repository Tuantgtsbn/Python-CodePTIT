import re
numTest=int(input())
def check(s):
    if(len(s)%2==1):
        return False
    else:
        
        
        if(s[::-1]!= s):

            return False
        else:

            if(re.search('[^02468]',s)):
                return False
            else:
                return True
        

for i in range(numTest):
    s=int(input())
    for i in range(s):
        if(check(str(i))):
            print(i,end=" ")
    print()