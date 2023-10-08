import math
import fractions
import decimal

class NV:
    index=0
    def __init__(self,name,mark_lt,mark_tt):
        NV.index+=1
        self.name=name
        self.mark_lt=mark_lt
        if(self.mark_lt>10):
            self.mark_lt/=10
        self.mark_tt=mark_tt
        
        if(self.mark_tt>10):
            self.mark_tt/=10
        self.id="TS0{}".format(NV.index)
        self.mark_tb=float((decimal.Decimal(self.mark_lt)+decimal.Decimal(self.mark_tt))/2)

        pass
    def review(self):
        if(self.mark_tb<5):
            return "TRUOT"
        elif(self.mark_tb<8):
            return "CAN NHAC"
        elif(self.mark_tb<=9.5):
            return "DAT"
        else:
            return "XUAT SAC"
    
    def print(self):
        print("{} {} {:.2f} {}".format(self.id,self.name,self.mark_tb,self.review()))
    
numTest=int(input())
ls_nv=[]
for i in range(numTest):
    a=NV(input(),float(input()),float(input()))
    ls_nv.append(a)

ls_nv.sort(key=lambda x: x.mark_tb,reverse=True)
for i in ls_nv:
    i.print()

