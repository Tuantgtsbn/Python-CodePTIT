numTest=int(input())
for i in range(numTest):
    n=int(input())
    Map={}
    Set=set()
    for x in input().split():
        Set.add(int(x))
        if(int(x) in Map.keys()):
            Map[int(x)]=Map[int(x)]+1
        else:
            Map[int(x)]=1
    max_appear=max(list(Map.values()))
    if(max_appear<=n//2):
        print("NO")
    else:
        for i in Set:
            if(Map[i]==max_appear):
                print(i)
                break