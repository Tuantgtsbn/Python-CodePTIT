n=int(input())
# a=[]
# for i in input().split():
#     tmp=int(i)
#     a.append(tmp)
a=[int(x) for x in input().split()]
index=0
while(index<len(a)):
    done=True
    i=index
    point=0
    for j in range(i,len(a)-1):
        if((a[j]+a[j+1])%2==0):
            point=j
            del a[j]
            del a[j]
            done=False
            break
    if(done):
        break
    else:
        if(point==0):
            index=0
        else:

            index=point-1

print(len(a))