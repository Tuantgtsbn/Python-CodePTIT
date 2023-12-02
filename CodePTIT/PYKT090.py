


f=open("D:\Python\CodePTIT\CONTACT.in")

s=f.readlines()
Set=set()
for i in s:
    i=i.strip().lower()
    Set.add(i)
ls=sorted([str(i) for i in Set])
for i in ls:
    print(i)

