
def thapHN(height,bd,tg,kt):
    if(height==1):
        print(bd,"->",kt)
        
    else:
        thapHN(height-1,bd,kt,tg)
        print(bd,"->",kt)
        thapHN(height-1,tg,bd,kt)



if __name__=='__main__':
    height=int(input())
    thapHN(height,'A','B','C')