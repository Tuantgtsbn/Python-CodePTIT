# n=int(input())
# arr=[int(x) for x in input().split()]
# stack=[]
# for i in arr:
#     if(len(stack)==0):
#         stack.insert(0,i)
#     else:
#         l=stack[0]
#         if((l+i)%2==0):
#             del stack[0]
#         else:
#             stack.insert(0,i)
# print(len(stack))
# import re
# numTets=int(input())
# for i in range(numTets):
#     s=input()
#     s.replace()
#     list_numbers=[int(x) for x in re.findall(r'\d+',s)]
#     print(min(list_numbers))


# a=[int(x) for x in input().split()]
# a.reverse()
# b=[int(x) for x in input().split()]
# b.reverse()
# c=[]
# l=max(len(a),len(b))
# if(len(a)<l):
#     a.append([0]*(l-len(a)))
# if(len(b)<l):
#     b.append([0]*(l-len(b)))
# nho=0
# for i in range(l):
#     s=a[i]+b[i]+nho
#     c.append(s%10)
#     nho=s//10
# if(nho>0):
#     c.append(nho)
# result=c[::-1]
# for i in result:
#     print(i,end="")

# import math
# f=open("D:\Python\CodePTIT\DATA.in",mode="r")
# result=[]
# lines=f.readlines()
# for line in lines:
#     words=line.split()
#     for word in words:
#         if(word.isdigit()):
#             if(int(word)<2147483648 and int(word)>-2147483648):
#                 continue
#             else:
#                 result.append(word)
#         else:
#             result.append(word)
# result.sort()
# for i in result:
#     print(i,end=" ")


# s="Nguyen Minh "
# a=s[:3]
# s.capitalize()
# print(a)
# s=s.strip("Nguyen ")
# print(s)
# delim = '.!?'
# import re
# lines=int(input())

# arr=[]
# dic={}
# unique=set()
# for i in range(lines):
#     text=input()
#     tmp=re.findall(r'\w+',text)
#     for j in tmp:
#         j=j.lower()
#         if(j not in unique):
#             unique.add(j)
#             dic[j]=1
#         else:
#             dic[j]=dic[j]+1;
# for i in dic:
#     arr.append((i,dic[i]))
# arr.sort(key=lambda x:(-x[1],x[0]))
# for i in arr:
#     print(i[0],i[1])

# import re
# delim1 = '.?!'
# delim2 = ':,'
# text = 'nguyen minh tuan: nam. Truong hoc : tuong giang .'
# # Nguyen minh tuan: nam
# # Truong hoc: tuong giang
# l = re.split('[.!?]', text)
# print(l)
# for j in l:
#     if (j != ''):
#         j = j.strip()
#         j=j[0].upper()+j[1:].lower()
#         print(type(j[1:]))
#         list_words = j.split()
#         print(list_words[0],end="")
#         for i in list_words[1:]:
#             if (i not in delim2):
#                 print(" ", i, sep="", end="")
#             else:
#                 print(i, end="")
#         print()

# from datetime import date,time,timedelta,datetime
# class Customer:
#     def __init__(self,name,room,checkin,checkout,index,phuphi) -> None:
#         self.name=name
#         self.room=room
#         self.checkin=checkin
#         self.checkout=checkout
#         self.id="KH{:02d}".format(index+1)
#         self.phuphi=phuphi
#         self.value=0
#         self.ngay=0

#         pass
#     def day(self):
#         date1=datetime.strptime(self.checkin,"%d/%m/%Y")
#         date2=datetime.strptime(self.checkout,'%d/%m/%Y')
#         lastDay=date2-date1
#         self.ngay=lastDay.days+1
#     def money(self):
#         floor=int(self.room[0])
#         value=0
#         self.day()
#         if(floor==1):
#             value+=25*self.ngay+self.phuphi
#         elif(floor==2):
#             value+=34*self.ngay+self.phuphi
#         elif(floor==3):
#             value+=50*self.ngay+self.phuphi
#         elif(floor==4):
#             value+=80*self.ngay+self.phuphi
#         self.value=value
    
#     def __str__(self) -> str:
#         return "{} {} {} {} {}".format(self.id,self.name,self.room,self.ngay,self.value)
#         pass

# if __name__=='__main__':
#     numTest=int(input())
#     ls=[]
#     for i in range(numTest):
#         cus=Customer(input(),input(),input(),input(),i,int(input()))
        
#         cus.money()
#         ls.append(cus)
#     ls.sort(key=lambda x:-x.value)
#     for i in ls:
#         print(i)
# '''
# 3
# Huynh Van Thanh
# 103
# 05/06/2010
# 05/06/2010
# 15
# Le Duc Cong
# 106
# 08/03/2010
# 01/05/2010
# 220
# Tran Thi Bich Tuyen
# 207
# 10/04/2010
# 21/04/2010
# 96
# '''

# from decimal import Decimal
# class GV:
#     def __init__(self,name,maxt,diemtin,diemcm,index) -> None:
#         self.name=name
#         self.maxt=maxt
#         self.id="GV{:02d}".format(index+1)
#         self.tong=float(0)
#         self.xeploai=""
#         self.diemtin=diemtin
#         self.diemcm=diemcm

#         pass
#     def __str__(self) -> str:
#         return "{} {} {} {:.1f} {}".format(self.id,self.name,self.mh(),self.tong,self.xeploai)
#         pass
#     def mh(self):
#         if(self.maxt[0]=='A'):
#             return 'TOAN'
#         elif(self.maxt[0]=='B'):
#             return 'LY'
#         else:
#             return 'HOA'
#     def update(self):
#         self.tong=float(Decimal(self.diemtin)*2+Decimal(self.diemcm))
#         if(self.maxt[1]=='1'):
#             self.tong+=2
#         elif(self.maxt[1]=='2'):
#             self.tong+=1.5
#         elif(self.maxt[1]=='3'):
#             self.tong+=1
        
#         if(self.tong>=18.0):
#             self.xeploai="TRUNG TUYEN"
#         else:
#             self.xeploai="LOAI"
# if __name__=='__main__':
#     numTest=int(input())
#     ls=[]
#     for i in range(numTest):
#         gv=GV(input(),input(),input(),input(),i)
#         gv.update()
#         ls.append(gv)

#     ls.sort(key=lambda x:x.tong,reverse=True)
#     for i in ls:
#         print(i)

# """
# 3
# Le Van Binh
# A1
# 7.0
# 3.0
# Tran Van Toan
# B3
# 4.0
# 7.0
# Hoang Thi Tam
# C2
# 7.0
# 6.0
# """

# n,m,k=[int(z) for z in input().split()]
# matrix=[]
# for i in range(n+1):
#     matrix.append([])
# for i in range(m):
#     x, y=[int(x) for x in input().split()]
#     matrix[x].append(y)
#     matrix[y].append(x)
# visited=[0]*(n+1)
# queue=[]
# queue.append(k)
# visited[k]=1
# while(len(queue)>0):
#     tmp=queue.pop() 
#     for i in matrix[tmp]:
#         if(visited[i]==0):
#             queue.append(i)
#             visited[i]=1
# flag=False
# for i in range(1,n+1):
#     if(visited[i]==0):
#         print(i)

# class SV:
#     def __init__(self,idSV,name,idClass) -> None:
#         self.idSV=idSV
#         self.name=name
#         self.idClass=idClass
#         self.cc=0
#         pass
#     def update(self,text):
#         sum=10
#         for i in text:
#             if(i=='v'):
#                 sum-=2
#             elif(i=='m'):
#                 sum-=1
#         if(sum<0):
#             self.cc=0
#         else:
#             self.cc=sum
# numTest=int(input())
# ls=[]
# for i in range(numTest):
#     sv=SV(input(),input(),input())
#     ls.append(sv)

# for i in range(numTest):
#     id,text=input().split()
#     for sv in ls:
#         if(sv.idSV==id):
#             sv.update(text)
# for sv in ls:
#     print("{} {} {} {}".format(sv.idSV,sv.name,sv.idClass,sv.cc),end="")
#     if(sv.cc==0):
#         print(" KDDK")
#     else:
#         print()
# from datetime import datetime,timedelta
# def cmp1(ls):
#     return datetime.strptime(ls[3],"%d/%m/%Y")
# def cmp2(ls):
#     return datetime.strptime(ls[4],"%H:%M")
# n,m=[int(x) for x in input().split()]
# dic={}
# for i in range(n):
#     idSub=input()
#     nameSub=input()
#     dic[idSub]=nameSub
# ls=[]
# for i in range(m):
#     tmp=[]
#     words=input().split()
#     tmp.append("T{:03d}".format(i+1))
#     tmp.append(words[0])
#     tmp.append(dic[words[0]])
#     for word in words[1:]:
#         tmp.append(word)
#     ls.append(tmp)

# ls.sort(key=lambda x:(cmp1(x),cmp2(x),x[1]))
# for i in ls:
#     print("{} {} {} {} {} {}".format(i[0],i[1],i[2],i[3],i[4],i[5]))

# ICPC0108
# for i in range(int(input())):
#     n=int(input())
#     a=[int(x) for x in input().split()]
#     a.sort()
#     s=0
#     for i in range(0,n-2):
#         l=i+1
#         r=len(a)-1
#         while(l<r):
#             if(a[i]+a[l]+a[r]==0):
#                 s+=1
#                 l+=1
#             elif(a[i]+a[l]+a[r]<0):
#                 l+=1
#             else:
#                 r-=1
#     print(s)


# ICPC0113
# import math
# mark=[1]*1000001
# mark[0]=mark[1]=0
# for i in range(2,int(math.sqrt(1000000))+1):
#     if(mark[i]==1):
#         for j in range(i*i,1000001,i):
#             mark[j]=0
# def check(n,m):
#     if(mark[n]==0):
#         return False
#     else:
#         number_to_string=str(n)
#         reverse_string=number_to_string[::-1]
#         if(mark[int(reverse_string)]==1 and number_to_string!=reverse_string and int(reverse_string)<m):
#             mark[int(reverse_string)]=0
#             return True
#         return False
# for i in range(int(input())):
#     n=int(input())
#     for i in range(n):
#         if(check(i,n)):
#             print(i,int(str(i)[::-1]),end=" ")
#     print()

# ICPC0114
# import math
# def checknt(n):
#     if(n<2):
#         return False
#     for i in range(2,int(math.sqrt(n))+1):
#         if(n%i==0):
#             return False
#     return True
# def sumcs(n):
#     sum=0
#     while(n!=0):
#         sum+=n%10
#         n//=10
#     return sum
# def check2(n):
#     while(n>0):
#         mod=n%10
#         if(checknt(mod)==False):
#             return False
#         n//=10
#     return True
# for i in range(int(input())):
#     n=int(input())
#     if(checknt(n) and checknt(int(str(n)[::-1])) and checknt(sumcs(n)) and check2(n)):
#         print("Yes")
#     else:
#         print("No")

# import math
# def round_decimal_up(number):
#     # Làm tròn số thập phân về số nguyên
#     rounded_number = round(number)
    
#     # Kiểm tra số đầu tiên phần thập phân, nếu lớn hơn hoặc bằng 5 thì làm tròn lên
#     decimal_part = number - rounded_number
#     if decimal_part >= 0.5:
#         rounded_number += 1
    
#     return rounded_number
# for i in range(int(input())):
#     n=int(input())
#     if(n<=10):
#         print(n)
#     else:
#         j=1
#         while(True):
#             n=round_decimal_up(n/(10**j))*(10**j)
            
#             if(n<10**(j+1)):
#                 break
#             j+=1
#         print(n)



# def round_decimal_up(number):
#     # Làm tròn số thập phân về số nguyên
#     rounded_number = round(number)
    
#     # Kiểm tra số đầu tiên phần thập phân, nếu lớn hơn hoặc bằng 5 thì làm tròn lên
#     decimal_part = number - rounded_number
#     if decimal_part >= 0.5:
#         rounded_number += 1
    
#     return rounded_number

# # Sử dụng hàm
# while(True):
#     result = round_decimal_up(float(input()))
#     print(result)  # Kết quả: 8


# a,k,n=[int(x) for x in input().split()]
# mod=k-int(a%k)
# step=mod
# check=False
# for i in range(mod,n-a+1,k):
#     check=True
#     if(i!=0):
#         print(i,end=" ")
# if(check==False):
#     print(-1)

# def tower(n,xp,tg,dich):
#     if(n==1):
#         print('{} -> {}'.format(xp,dich))
#         return
#     else:
#         tower(n-1,xp,dich,tg)
#         print('{} -> {}'.format(xp,dich))
#         tower(n-1,tg,xp,dich)
    



# num=int(input())
# tower(num,'A','B','C')



# def Try(s,l,a,b,c):
#     if(len(s)==l):
#         if(a<=b and b<=c and a>0):
#             print(s)
#             return
#     else:
#         Try(s+"A",l,a+1,b,c)
#         Try(s+"B",l,a,b+1,c)
#         Try(s+"C",l,a,b,c+1)
# for i in range(3,int(input())+1):
    
#     Try('',i,0,0,0)
# from itertools import combinations_with_replacement,permutations,combinations
# n,k=[int(x) for x in input().split()]
# unique=set([int(x) for x in input().split()])
# ls=combinations(unique,k)
# for i in ls:
#     for j in i:
#         print(j,end=" ")
#     print()
# def result(n):
#     sum=1
#     while(n!=1):
#         if(n%2==0):
#             n=n//2
#         else:
#             n=n*3+1
#         sum+=1
#     return sum

# while(True):
#     n=int(input())
#     if(n==0):
#         break
#     print(result(n))

# st=[]
# ans=[]
# for i in range(int(input())):
#     n=int(input())
#     ls=[int(x) for x in input().split()]
#     for i in range(n):
#         while(len(st)>0 and ls[i]>=ls[st[-1]]):
#             st.pop()
#         if(len(st)==0):
#             ans.append(i+1)
#         else:
#             ans.append(i-st[-1])
#         st.append(i)
# for i in ans:
#     print(i,end=" ")


# t = int(input())
# for z in range(t) :
#     n, m = [int(x) for x in input().split()]
#     a = [[0]] * n
#     b = [[0]] * 3
#     s = 0
#     for i in range(n) : a[i] = [int(x) for x in input().split()]
#     for i in range(3) : b[i] = [int(x) for x in input().split()]
#     for i in range(2, n) :
#         for j in range(2, m) :
#             s += a[i - 2][j - 2] * b[0][0] 
#             s += a[i - 2][j - 1] * b[0][1]
#             s += a[i - 2][j] * b[0][2]
#             s += a[i - 1][j - 2] * b[1][0]
#             s += a[i - 1][j - 1] * b[1][1]
#             s += a[i - 1][j] * b[1][2]
#             s += a[i][j - 2] * b[2][0]
#             s += a[i][j - 1] * b[2][1]
#             s += a[i][j] * b[2][2]
#     print(s)

# def hi(matrixa,matrixb):
#     sum=0
#     for i in range(3):
#         for j in range(3):
#             sum+=matrixa[i][j]*matrixb[i][j]
#     return sum
# t=int(input())
# for test in range(t):
#     n,m=[int(x) for x in input().split()]
#     ls=[]
    
#     for j in range(n):
#         tmp=[int(x) for x in input().split()]
#         ls.append(tmp)
#     k=[]
#     for i in range(3):
#         tmp=[int(x) for x in input().split()]
#         k.append(tmp)
#     result=0
#     for x in range(n-2):
#         for y in range(m-2):
            
#             result+=hi([ls[x][y:y+3],ls[x+1][y:y+3],ls[x+2][y:y+3]],k)
#     print(result)
from datetime import datetime, time, timedelta

# str_arrive = "08:00"
# str_left = "17:00"
# str_eat = "01:00"
# str_chuan = "08:00"

# # Chuyển đổi thành đối tượng time
# arrive = datetime.strptime(str_arrive, "%H:%M").time()
# left = datetime.strptime(str_left, "%H:%M").time()
# eat = datetime.strptime(str_eat, "%H:%M").time()
# chuan = datetime.strptime(str_chuan, "%H:%M").time()

# # Tính tổng thời gian làm việc
# tong = timedelta(hours=left.hour - arrive.hour, minutes=left.minute - arrive.minute) - timedelta(hours=eat.hour, minutes=eat.minute)
# if(tong>=timedelta(hours=chuan.hour,minutes=chuan.minute)):
#     print("DU")
# else:
#     print("THIEU")
# s=tong.__str__()
# print(s,4)
# date1=datetime.strptime("28/07/2003 12:11","%d/%m/%Y %H:%M")
# date2=datetime.strptime("29/07/2003 14:11","%d/%m/%Y %H:%M")
# a=date2-date1
# print(a.seconds)
# def caesar_cipher(text, shift):
#     result = ""
#     for char in text:
#         if char.isalpha():
#             shift_amount = shift % 26
#             if char.islower():
#                 shifted_char = chr(((ord(char) - 97 + shift_amount) % 26) + 97)
#             else:
#                 shifted_char = chr(((ord(char) - 65 + shift_amount) % 26) + 65)
#             result += shifted_char
#         else:
#             result += char
#     return result

# text = "Hello, World!"
# shift = -2
# encrypted_text = caesar_cipher(text, shift)
# print(encrypted_text)  # Mjqqt, Btwqi!
print(-2%26)