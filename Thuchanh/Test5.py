file=open("D:\Python\Thuchanh\CATHI.in",mode='r')
ds1=list(file)
ds2=[]
nCathi=int(ds1[0])
index=1
for i in range(1,nCathi+1,1):
    caThi={}
    caThi['date']=ds1[index].strip()
    index+=1
    caThi['time']=ds1[index].strip()
    index+=1
    caThi['phong']=ds1[index].strip()
    index+=1
    # caThi['id']='C'+"{:03}".format(i)
    if(i<10):
        caThi['id']="C00"+str(i)
    elif(i<100):
        caThi['id']="C0"+str(i)
    else:
        caThi['id']="C"+str(i)
    ds2.append(caThi)
ds3=sorted(ds2,key=lambda caThi:(caThi['date'][-4:],caThi['date'][3:5],caThi['date'][0:2],caThi['time'],caThi['id']))
for caThi in ds3:
    print(caThi.get('id'),caThi.get('date'),caThi.get('time'),caThi.get('phong'))