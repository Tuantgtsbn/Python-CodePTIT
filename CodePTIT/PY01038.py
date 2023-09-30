numTest=int(input())
for i in range(numTest):
    number=int(input())
    sum=number
    cnt=0
    while(sum%7!=0  and cnt<=1000):
        number_reverse=int(str(sum)[::-1])
        sum+=number_reverse
        cnt+=1
    if(cnt>1000):
        print(-1)
    else:
        print(sum)