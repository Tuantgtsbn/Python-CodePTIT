num=int(input())
arr=list(map(int,input().split()))
cnt=0
for i in range(1,num):
    if(arr[i]!=arr[i-1]):
        cnt+=1
print(cnt)