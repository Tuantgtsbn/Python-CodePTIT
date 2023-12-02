import math
import re
def tinhtoan(s):
    l=len(s)
    while(len(s)%3!=0):
        s='0'+s
    result=""
    ls=re.findall(r'\d{3}',s)
    for i in ls:
        sum=0
        for j in range(3):
            sum+=(2**j)*int(i[2-j])
        result+=str(sum)
    print(result)
tinhtoan(input())

