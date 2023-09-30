import decimal as dc
import math
list1={"A":10,"B":10,"C":9, "D":8}
list2={"A":12,"B":11,"C":10,"D":9}
list3={"A":14,"B":13,"C":12,"D":11}
list4={"A":20,"B":16,"C":14,"D":13}

class NV:
    def __init__(self,id,ten,lcb,nc):
        self.id=id
        self.ten=ten
        self.pb=""
        self.lt=0
        self.lcb=lcb
        self.nc=nc
        self.hs=0
        pass
    def heso(self):
        ma=self.id[0]
        nam=int(self.id[1:3])
        if(1<=nam and nam<=3):
            self.hs=list1.get(ma)
        elif(4<=nam and nam<=8):
            self.hs=list2.get(ma)
        if(9<=nam and nam<=15):
            self.hs=list3.get(ma)
        elif(nam>=16):
            self.hs=list4.get(ma)
    def tienluong(self):
        self.lt=self.nc*self.lcb*self.hs*1000

numTest=int(input())
List1={}
List2=[]
for i in range(numTest):
    s=input().strip()
    List1[s[0:2]]=s[3:]
sl=int(input())
for i in range(sl):
    id=input()
    ten=input()
    lcb=int(input())
    nc=int(input())
    nv=NV(id,ten,lcb,nc)
    nv.heso()
    nv.tienluong()
    nv.tienluong()
    id_pb=id[-2:]
    nv.pb=List1.get(id_pb)
    List2.append(nv)
for nv in List2:
    print("{} {} {} {}".format(nv.id,nv.ten,nv.pb,nv.lt))


    
