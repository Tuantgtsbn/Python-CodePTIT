number=input()
len_number=len(number)
result=""
number_of_dau=len_number//3
for i in range(1,len_number+1,1):
    if(i%3!=0 or i==len_number):
        result=number[-i]+result
    else:
        result=","+number[-i]+result
print(result)