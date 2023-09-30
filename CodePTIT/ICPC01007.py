# numTest=int(input())
# for j in range (numTest):
#         p,q=[x for x in input().split()]
#         x1 = input().strip()
#         if(x1.count(' ')) : x1,x2 = x1.split()
#         else : x2 = input()
        
#         max=max(p,q)
#         min=min(p,q)
#         x1=x1.replace(max,min)
#         x2=x2.replace(max,min)
#         minSum=int(x1)+int(x2)
#         print(minSum,end=" ")
#         x1=x1.replace(min,max)
#         x2=x2.replace(min,max)
#         maxSum=int(x1)+int(x2)
#         print(maxSum)
        
t = int(input())
for i in range(t) : 
    m, n = [x for x in input().split()]
    a = input().strip()
    if(a.count(' ')) : a, b = a.split()
    else : b = input()
    p = min(m, n)
    q = max(m, n)
    print(int(a.replace(q, p)) + int(b.replace(q, p)), end=" ")
    print(int(a.replace(p, q)) + int(b.replace(p, q)))