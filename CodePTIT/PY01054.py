numTest=int(input())
for i in range(numTest):
    string=input()
    times=1
    for i in string:
        if(i!='0'):
            times*=int(i)
    print(times)