from decimal import *
import math
from fractions import *
numTest=int(input())
for i in range(numTest):
    number=int(input())
    sum=0
    if(number%2==0):
        for j in range(2,number+1,2):
            sum+=Fraction(1,j)
    else:
        for j in range(1,number+1,2):
            sum+=Fraction(1,j)
    print("{:.6f}".format(float(sum)))
