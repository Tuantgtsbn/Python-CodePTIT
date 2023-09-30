import decimal
import math
import fractions
const=math.sqrt(5)
numTest=int(input())
List=[]
for i in range(numTest):
    n=int(input())
    a=int((decimal.Decimal('3')+decimal.Decimal(str(const)))**n)
    a=a%1000
    # print("Case #{}: {:03d}".format(i+1,a))
    List.append("Case #{}: {:03d}".format(i+1,a))
for i in List:
    print(i)
