

n,k=[int(x) for x in input().split()]
k-=1
ls=[]
ls1=[int(x) for x in input().split()]
ls2=[int(x) for x in input().split()]
for i in range(n):
    ls.append([ls1[i],ls2[i],ls1[i]-ls2[i]])
ls.sort(key=lambda x: x[2])
sum=0;
for i in range(n):
    if(i<=k):
        sum+=ls[i][0]
    else:
        if(ls[i][2]>=0):
            sum+=ls[i][1]
        elif(ls[i][2]<0):
            sum+=ls[i][0]
print(sum)