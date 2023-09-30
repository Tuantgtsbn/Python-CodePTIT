# import math
# import re


# mark=[1]*10000001
# mark[0]=mark[1]=0
# for i in range(2,int(math.sqrt(10000000))+1,1):
#     if mark[i]==1:
#         for j in range(i*i,10000001,i):
#             mark[j]=0
# numTest=int(input())
# for i in range(numTest):
    
#     n=int(input())
#     tmp=int(str(n)[::-1])
#     # print(n,tmp)
#     kq=1
#     if(mark[n]==1 and mark[tmp]==1):
#         sum=0
        
#         while(n!=0):
#             md=int(n%10)
            
#             if(mark[md]!=1):
#                 kq=0
#                 break
#             n//=10
#             sum+=md
#         if(kq==0):
#             print("No")
#         elif mark[sum]==1:
#             print("Yes")
#         else:
#             print("No")
#     else:
#         print("No")



import math
def nto(n) :
    if n < 2 : return False
    for i in range(2, int(math.sqrt(n)) + 1) :
        if n % i == 0 : return False
    return True
def check(n) :
    m = 0
    s = 0
    x = n
    while n != 0 :
        k = n % 10
        if nto(k) == False : return False
        m = m * 10 + k
        s += k
        n = int(n / 10)
    if nto(s) and nto(x) and nto(m) : return True
    return False
t = int(input())
for i in range(t) :
    n = int(input())
    if check(n) == True : print("Yes")
    else : print("No")