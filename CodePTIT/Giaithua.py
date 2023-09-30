def giaithua(number):
    if(number==0):
        return 0
    else:
        arr=[0]*(number+1)
        arr[1]=1
        for i in range(2,number+1,1):
            arr[i]=arr[i-1]*i
        return arr[number]
    
