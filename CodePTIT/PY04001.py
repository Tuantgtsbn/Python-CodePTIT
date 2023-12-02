from decimal import Decimal
import math
class Point:
    def __init__(self,a,b):
        self.x=Decimal(a)
        self.y=Decimal(b)
        
        pass
    def distance(self,a):
        f=math.sqrt(math.pow(self.x-a.x,2)+math.pow(self.y-a.y,2))
        return "%.4f"%f

if __name__ == '__main__':
    # context=getcontext()
    # context.prec=4
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1