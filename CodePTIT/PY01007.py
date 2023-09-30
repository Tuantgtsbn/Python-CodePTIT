import math
numTest=int(input())
for i in range(numTest):
    n,x,m=[float(x) for x in input().split()]
    year=math.ceil(math.log(m/n,1+x/100))
    print(year)