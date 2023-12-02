# import math
# import decimal
# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#         pass
    
# def distance(p1,p2):
#     return math.sqrt(math.pow(p1.x-p2.x,2)+math.pow(p1.y-p2.y,2))
# class Triangle:
#     def __init__(self,p1,p2,p3):
#         self.p1=p1
#         self.p2=p2
#         self.p3=p3
#         self.d1=0
#         self.d2=0
#         self.d3=0
#         pass
#     def check(self):
#         self.d1=decimal.Decimal(distance(self.p1,self.p2))
#         self.d2=decimal.Decimal(distance(self.p2,self.p3))
#         self.d3=decimal.Decimal(distance(self.p3,self.p1))
#         if(self.d1+self.d2==self.d3 or self.d2+self.d3==self.d1 or self.d1+self.d3==self.d2):
#             return False
#         else:
#             return True
#     def result(self):
#         if(not self.check()):
#             return "INVALID"
#         else:
#             return "{:.3f}".format(self.d1+self.d2+self.d3)
# if __name__=='__main__':
#     numTest=int(input())
#     ls=[]
#     for i in range(numTest):
#         arr=list(map(float,input().split()))
#         t=Triangle(Point(arr[0],arr[1]),Point(arr[2],arr[3]),Point(arr[4],arr[5]))
#         ls.append(t.result())
#     for i in ls:
#         print(i)
# Lazygarde

import math

class Point :
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, k) :
        x0 = self.x - k.x
        y0 = self.y - k.y
        return math.sqrt(x0 * x0 + y0 * y0)

class Triangle :
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    def cnt(self) :
        a = self.p1.distance(self.p2)
        b = self.p2.distance(self.p3)
        c = self.p1.distance(self.p3)
        if(max(a, b, c) * 2 >= a + b + c) : print('INVALID')
        else : print('{:.3f}'.format(a + b + c))

a = []
t = int(input())
for x in range(t):
    a += [float(i) for i in input().split()]
i = 0
for index in range(t):
    triagle = Triangle(Point(a[i], a[i+1]), Point(a[i+2], a[i+3]), Point(a[i+4], a[i+5]))
    triagle.cnt()
    i += 6
    
''' Do Xuan Huong
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@##################@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@#############################@@@@@@@@@@@@@@@@
@@@@@@@@@@@@&####################################@@@@@@@@@@@@
@@@@@@@@@@##########################################@@@@@@@@@
@@@@@@@@##############################################@@@@@@@
@@@@@@#################################################@@@@@@
@@@@@####################################################@@@@
@@@%#####################@@@@@@@@@@@######################@@@
@@@###################@@@@@@@@@@@@@@@@@####################@@
@@##################@@@@@@         @@@@@@##################@@
@@#################@@@@@             @@@@###################@
@@@@@@@@@@@@@@@@@@@@@@@@             @@@@@@@@@@@@@@@@@@@@@@@@
@                  &@@@@             @@@@           .......@@
@@                  @@@@@@         @@@@@@           .......@@
@@                    @@@@@@@@@@@@@@@@@            .......@@@
@@@                      @@@@@@@@@@@               ......@@@@
@@@@                                              ......@@@@@
@@@@@@                                           ......@@@@@@
@@@@@@@                                         .....@@@@@@@@
@@@@@@@@@                                     .....@@@@@@@@@@
@@@@@@@@@@@@                                ....@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@                         ....@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@%                .@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
'''