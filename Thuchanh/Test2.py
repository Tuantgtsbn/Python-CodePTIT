file=open('D:\Python\Thuchanh\CONTACT.in',mode='r')
ds1=list(file)
# print(ds1)
for i in range(len(ds1)):
    ds1[i]=ds1[i].strip()
ds2=set()
for i in ds1:
    ds2.add(i.lower())
ds3=sorted(ds2)
for i in ds3:
    print(i)
