numTest=int(input())
for i in range(numTest):
    s=input()
    result=""
    i=0
    while i<len(s):
        repeat=1
        if(i==len(s)-1):
            result+="1"+s[i]
            i+=1
        else:
            while(i<len(s)-1 and s[i+1]==s[i]):
                repeat+=1
                i+=1
            result+=str(repeat)+s[i]  
            i+=1  
    print(result)
        
