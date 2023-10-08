import math
class user:
    def __init__(self,id,name,start,end):
        self.id=id
        self.name=name
        self.start=start
        self.end=end
        self.hours=0
        pass
    def print(self):
        print("{} {} {}".format(self.id,self.name,self.chuanhoa()))
    def hour(self):
        h_start=int(self.start[:2])
        m_start=int(self.start[-2:])
        h_end=int(self.end[:2])
        m_end=int(self.end[-2:])
        self.hours=(h_end*60+m_end)-(h_start*60+m_start)
    def chuanhoa(self):
        a=self.hours
        h=a//60
        m=a%60
        return "{} gio {} phut".format(h,m)
        

numTest=int(input())
ls_player=[]
for i in range(numTest):
    a=user(input(),input(),input(),input())
    a.hour()
    ls_player.append(a)
ls_player.sort(key=lambda x:x.hours,reverse=True)
for i in ls_player:
    i.print()