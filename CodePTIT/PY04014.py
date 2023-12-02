from decimal import Decimal
class SinhVien:
    def __init__(self,nameSV,string,index) :
        self.id="HS{:02d}".format(index+1)
        self.nameSV=nameSV
        self.tb=0.0
        self.sumMark=Decimal('0')
        arr=string.split()
        for i in range(len(arr)):
            if(i==0 or i==1):
                self.sumMark+=Decimal(arr[i])*2
            else:
                self.sumMark+=Decimal(arr[i])
        ##print(self.sumMark)
        pass
    def update(self):
        self.tb=float(self.sumMark/12)
        # print(self.tb)
    def xepLoai(self):
        
        if(self.tb<5):
            return "YEU"
        elif(self.tb<7):
            return "TB"
        elif(self.tb<8):
            return "KHA"
        elif(self.tb<9):
            return "GIOI"
        else:
            return "XUAT SAC"

if __name__=='__main__':
    numTest=int(input())
    ls=[]
    for i in range(numTest):
        sv=SinhVien(input().strip(),input(),i)
        sv.update()
        ls.append(sv)
        
    ls.sort(key=lambda x:(-x.tb,x.id),reverse=False)
    for i in ls:
        print(i.id+" "+i.nameSV+" "+"{:.1f} ".format(round(i.tb,2))+i.xepLoai())
