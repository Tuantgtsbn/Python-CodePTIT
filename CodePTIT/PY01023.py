import math
numTest=int(input())
def prime(number):
    s="1"
    for i in range(2,int(math.sqrt(number))+1,1):
        if(number%i==0):
            cnt=0
            while number%i==0:
                cnt+=1
                number//=i
            # s=s+" "+str(i)+"^"+cnt
            s="{} * {}^{}".format(s,i,cnt)
    if(number!=1):
        s="{} * {}^{}".format(s,number,1)
    return s
        
    
for i in range(numTest):
    number=int(input())
    print(prime(number))
