import decimal
import math

KV={1:1.5,2:1,3:0}
DT=[{'Kinh',0}]

class TS:
    def __init__(self,ten,diem,dtoc,kvuc):
        self.ten=ten
        self.diem=diem
        self.dtoc=dtoc
        self.kvuc=kvuc
        self.id=""
        pass
    def chuanhoaten(self):
        tmp=self.ten.strip()
        List=tmp.split()
        new_name=""
        for i in List:
            new_name+=i.title()+" "
        new_name=new_name.strip()
        self.ten=new_name
    def diemcong(self):
        dc=0
        if(self.dtoc!="Kinh"):
            dc=1.5
        dc+=KV.get(self.kvuc,0)
        return dc
    def tongdiem(self):
        return decimal.Decimal(self.diem)+decimal.Decimal(self.diemcong())
    def check(self):
        if(self.tongdiem()>=20.5):
            return "Do"
        return "Truot"

numTest=int(input())
List=[]
for i in range(numTest):
    name=input()
    diem=float(input())
    dtoc=input()
    kvuc=int(input())
    ts=TS(name,diem,dtoc,kvuc)
    ts.id="TS"+"{:02d}".format(i+1)
    ts.chuanhoaten()
    List.append(ts)
List.sort(key=lambda x:(-1*x.tongdiem(),x.id))
for i in List:
    print("{} {} {:.1f} {}".format(i.id,i.ten,i.tongdiem(),i.check()))
    
    
