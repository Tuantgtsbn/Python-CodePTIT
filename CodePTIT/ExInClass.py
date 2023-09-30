#In ra so chia het cho 5 va 9
# for i in range(1100,3901): 
#     if i%5==0 and i%9==0:
#         print(i,end=" ")
# import re
# s=input()
# a=re.findall('\d+',s)
# sum=0
# for i in a:
#     sum+=len(i)
# print(sum)


# list_subjects=[("English",88),("Science",90),("Maths",97),("Social sciences",82)]

# list_sorted=sorted(list_subjects,key=lambda x:x[1])
# print(list_sorted)

from Giaithua import giaithua
number=int(input())
print(giaithua(number))