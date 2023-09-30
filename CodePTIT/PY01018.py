P="ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
import sys
def check2(s):
    return 10
if __name__=="__main__":
    while(True):
        List=input().split()
        k=int(List[0])
        if(k==0): sys.exit(0)
        s=List[1]
        tmp=""
        for i in range(len(s)):
            tmp+=P[(P.index(s[i])+k)%28]
        print(tmp[::-1])
