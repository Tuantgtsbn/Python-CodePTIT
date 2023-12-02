import math
mark=[1]*10000001
mark[0]=mark[1]=0
for i in range(2,int(math.sqrt(10000000))+1,1):
    if(mark[i]==1):
        for j in range(i*i,10000001,i):
            mark[j]=i
cnt=[0]*10000001
cnt[1]=1
for i in range(2,10000001,1):
    if(mark[i]==1):
        cnt[i]=2
    else:
        start=mark[i]
        repeat=1
        while(i%(int(math.pow(start,repeat)))==0):
            repeat+=1
        cnt[i]=repeat*cnt[i//int(math.pow(start,repeat-1))]
max_left=[0]*10000001
max_left[1]=1
for i in range(2,10000001,1):
    max_left[i]=max(max_left[i-1],cnt[i])
def is_true(number):
    if(max_left[number-1]<cnt[number]):
        return True
    else:
        return False

numTest=int(input())
# print(cnt)
for i in range(numTest):
    number=int(input())
    while True:
        if(is_true(number)):
            print(number)
            break
        else:
            number+=1


