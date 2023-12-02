import math
class PhanSo:
    def __init__(self,tu,mau):
        self.tu=tu
        self.mau=mau
        pass
    def Print(self):
        ucll=math.gcd(self.tu,self.mau)
        print('{}/{}'.format(int(self.tu/ucll),int(self.mau/ucll)))
    def update(self,tu,mau):
        self.tu=tu
        self.mau=mau
    def tong(self,a):
        bcnn=math.lcm(self.mau,a.mau)
        tu=int(bcnn/self.mau)*self.tu+int(bcnn/a.mau)*a.tu
        return PhanSo(tu,bcnn)
if __name__=='__main__':
    s=input().split()
    ps1=PhanSo(int(s[0]),int(s[1]))
    ps2=PhanSo(int(s[2]),int(s[3]))
    ps1.tong(ps2).Print()