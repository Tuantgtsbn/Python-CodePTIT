import re
numTest=int(input())
for i in range(numTest):
    pattern=r"\d+"
    s=input()
    b=re.findall(pattern,s)
    d=re.findall('\w{4}',s)
    c=[int(x) for x in b]
    print(d)
    
    print(max(c))
