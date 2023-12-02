import math
cc=['0','1','2','3','4','5','6','7','8','9','A','B','C','D'
    ,'E','F','G','H','I','j','K','L','M','N','O','P','Q','R',
    'S','T','U','V','W','X','Y','Z']
def doicoso(a,b):
    ls=[]
    while(a!=0):
        ls.append(cc[a%b])
        a//=b
    for i in range(len(ls)):
        print(ls[-(i+1)],end="")
numTest=int(input())
for i in range(numTest):
    a,b=[int(x) for x in input().split()]
    doicoso(a,b)
    print()