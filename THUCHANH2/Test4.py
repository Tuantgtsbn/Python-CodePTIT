

File=open("THUCHANH2\DATA.in")
a=2147483647
b=-2147483648
List=[]
for line in File:
    line=line.rstrip()
    
    # print(line)
    # print(line.split())
    for word in line.split():
        if word.isnumeric() and b<=int(word) and int(word)<=a:
            continue
        else:
            List.append(word)
for i in sorted(List):
    print(i,end=" ")
