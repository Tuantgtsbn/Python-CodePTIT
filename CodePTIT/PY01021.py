numTest=int(input())
for i in range(numTest):
    line=input()
    sum=0
    ls=[]
    for i in line:
        if(i.isdigit()):
            sum+=int(i)
        else:
           ls.append(i) 
    ls.sort()
    ls.append(sum)
    for i in ls:
        print(i,end="")
    print()

    