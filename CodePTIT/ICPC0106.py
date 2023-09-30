import re
import math
def tachchuoi(cs,xnp):
    if(cs==1):

        List=re.findall('\w{1}',xnp)
    elif(cs==2):
        List=re.findall('\w{2}',xnp)
    elif(cs==3):
        List=re.findall('\w{3}',xnp)
    elif(cs==4):
        List=re.findall('\w{4}',xnp)

    lenxnp=len(xnp)
    du=lenxnp%cs
    if(du!=0):
        List.append(xnp[-du:])
    return List
bangtracu=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
def value(str,cs):
    sum=0
    for i in range(len(str)):
        sum+=int(int(str[i])*(2**i))
    return bangtracu[sum]

def solve(cs,xnp):
    xnp=xnp[::-1]
    result=""
    List=tachchuoi(cs,xnp)
    for i in List:
        result=value(i,cs)+result
    return result

if __name__=='__main__':
    numTest=int(input())
    for j in range(numTest):
        cs=int(input())
        mu=int(math.log2(cs))
        
        xnp=input()
        print(solve(mu,xnp),end='\n')
        