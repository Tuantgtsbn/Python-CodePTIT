
numTest=int(input())
dic={}
for i in range(numTest):
    maId=input()
    name=input()
    exam=input()
    dic[maId]=[name,exam]
lsId=list(dic.keys())
lsId.sort()
for i in lsId:
    print("{} {} {}".format(i,dic[i][0],dic[i][1]))
