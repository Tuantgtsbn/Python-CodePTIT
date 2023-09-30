# import re
# numTest=int(input())
# for i in range(numTest):
#     s=input()
#     lens=len(s)
#     if(lens==1):
#         print(s)
#     else:
#         List=re.findall('\d{1}',s)
#         List=[int(x) for x in List]
        
#         # print(List)
#         nho=0
#         for j in range(lens-2,-1,-1):
#             # print(List[j])
#             if(List[j+1]>=5):
#                 List[j]=List[j]+nho+1
#                 nho=int(List[j]/10)
#                 List[j]=int(List[j]%10)
#                 List[j+1]=0
#             else:
#                 List[j]=List[j]+nho
#                 nho=int(List[j]/10)
#                 List[j]=int(List[j]%10)
#                 List[j+1]=0

        
#         if(nho!=0):
#             print(nho)
#             List.insert(0,nho)
#         result=""
#         for i in List:
#             result+=str(i)
#         print(result)
                
t = int(input())
for i in range(t) :
    s = input()
    ans = ""
    ok = 1
    for i in range(1, len(s)) :
        ans += "0"
        if ok == 0 :
            if int(s[-i]) > 3 :
                ok = 0
            else :
                ok = 1
        else :
            if int(s[-i]) > 4 :
                ok = 0
            else :
                ok = 1
    if ok == 0 :
        if int(s[0]) == 9 :
            ans += "0"
            ans = "1" + ans
        else :
            ans = chr(ord(s[0]) + 1) + ans
    else : ans = s[0] + ans
    print(ans)