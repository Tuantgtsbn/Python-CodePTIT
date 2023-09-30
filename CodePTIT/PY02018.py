n=int(input())
Set=set()
for i in input().split():
    Set.add(int(i))
i=1
while True:
    if i not in Set:
        print(i)
        break
    else:
        i+=1
