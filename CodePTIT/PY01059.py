numTest=int(input())
for i in range(numTest):
    number=input()
    sum_index_even=0
    times_index_odd=1
    # mark_zero=False
    for j in range(len(number)):
        if(j%2==1):
            sum_index_even+=int(number[j])
        else:
            if(int(number[j])!=0):
                # mark_zero=True
                times_index_odd*=int(number[j])
    
    print(times_index_odd,sum_index_even)
    