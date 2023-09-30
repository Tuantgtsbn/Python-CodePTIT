# import math
# n=int(input())
# mark=[1]*12000
# a=[int(x) for x in input().split()]
# mark[0]=0
# mark[1]=0
# for i in range(2,int(math.sqrt(12000)),1):
#     if(mark[i]==1):
#         for j in range(i*i,12000,i):
#             mark[j]=0

# z=[]
# for i in range(n):
#     tmp=a[i]
#     tmp2=tmp
#     dis1=0
#     dis2=0
#     while(mark[tmp]!=1):
#         dis1+=1
#         tmp+=1
#     while(mark[tmp2]!=1):
#         dis2+=1
#         tmp2-=1
#     z.append(min(dis1,dis2))

# print(max(z))
# n=int(input())
# class SV:
#     def __init__(self,id,name,lop,diem=10,diemdanh="",dg=""):
#         self.id=id
#         self.name=name
#         self.lop=lop
#         self.diemdanh=diemdanh
#         self.dg=dg
#         self.diem=diem
#         pass

# if __name__=="__main__":
#     ListSv=[]
# for i in range(n):
#     id=input()
#     name=input()
#     lop=input()
#     ListSv.append(SV(id,name,lop))
# for i in range(n):
#     s=input()
#     ListTmp=s.split()
#     id=ListTmp[0]
#     diemdanh=ListTmp[1]
#     for sv in ListSv:
#         if sv.id ==id:
#             sv.diemdanh=diemdanh
#             for i in diemdanh:
#                 if i=='m':
#                     sv.diem-=1
#                 elif i=='o':
#                     sv.diem-=2
#             if sv.diem<=0:
#                 sv.dg="KDDKDT"
#             else:
#                 sv.dg='DDKDT'
#             break
# for sv in ListSv:
#     print(sv.id,sv.name,sv.lop,sv.dg,sep=" ",end="\n")

    


# studen_data={
#     'id1':
#     {
#         'name':'Sara',
#         'class':'V',
#         'subject':['english','math','science']
#     },
#     'id2':
#     {
#         'name':'David',
#         'class':'V',
#         'subject':['english','math','science']
#     },
#     'id3':
#     {
#         'name':'Sara',
#         'class':'V',
#         'subject':['english','math','science']
#     },
#     'id4':
#     {
#         'name':'Surya',
#         'class':'V',
#         'subject':['english','math','science']
#     },

# }

# filt_data={}
# for key,value in studen_data.items():
#     if value not in filt_data.values():
#         filt_data[key]=value
# print(filt_data)


# words=['Red','Green','Red','Blue','Red','Green','Red']

# a=set()
# result={}
# for i in words:
#     if i not in a:
#         a.add(i)
#         result[i]=1
#     else:
#         result[i]+=1
# print(result)


# List=['pqrefgh','pqrsfgh','pqrsfjfjgj']
# min_length_word=min([len(x) for x in List])
# result=""
# len_list=len(List)
# for i in range(min_length_word):
#     set_word=set()
#     for j in range(len_list):
#         set_word.add(List[j][i])
#     if(len(set_word)==1):
#         result+=List[0][i]
# print(result)

# file=open("D:\Python\A.txt")
# list_A=[]
# for i in file:
#     list_A.append(i)
# file.close()

# list_B=[]
# file=open("D:\Python\B.txt")
# for i in file:
#     list_B.append(i)
# n=len(list_A)
# # print(list_A)
# # print(list_B)
# for i in range(n):
#     try:
#         list_A[i]=int(list_A[i].strip())
#         list_B[i]=int(list_B[i].strip())
#     except Exception:
#         print("Loi dinh dang")
#         pass
#         # list_A.pop()
#         # list_B.pop()
#     else:
#         print(list_A[i]**list_B[i])
import math
text="my mother is a person i admire most. she devoted a lot of time and energy to the upbringing of my two brothers and 1. despite working hard, she always made time to teach us many useful things which are necessary and important in our later lives. moreover, she is a good role model for me to follow. she always tries to get on well with people who live next door and help everyone when they are in difficulties, so most of them respect and love her. i admire and look up to my mother because she not only brings me up well but also stands by me and gives some help if necessary. for example, when i encounter some difficulties, she will give me some precious advice to help me solve those problems. she has a major influence on me and 1 hope that i will inherit some of her traits."
list_words=text.split()
arr=['.','!','?']
max1=0
for i in list_words:
    if(i[len(i)-1] in arr):
        max1=max(max1,len(i)-1)
    else:
        max1=max(max1,len(i))
        
print(max1)