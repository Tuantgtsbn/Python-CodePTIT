# numTest=int(input())
# def ptnt(n,p):
#     cnt=0
#     while(n%p==0):
#         cnt+=1
#         n/=p
#     return cnt
# for i in range(1,100001,1):
#     a[i]=ptnt()
# for i in range(numTest):
#     p,q=[int(x) for x in input().split()]
#     result=0
#     for j in range(1,p+1,1):
#         result+=ptnt(j,q)
#     print(result)

import math

# Hàm tính số lượng thừa số nguyên tố p trong N!
def count_factors_in_fact(N, p):
    count = 0
    while N >= p:
        N //= p
        count += N
    return count

# Đọc số lượng bộ test
T = int(input())

for _ in range(T):
    # Đọc N và p
    N, p = map(int, input().split())
    
    # Tính số lượng thừa số nguyên tố p trong N!
    count_p = count_factors_in_fact(N, p)
    
    # Tìm số lớn nhất x sao cho p^x <= count_p
    # x = 0
    # while p**x <= count_p:
    #     x += 1
    
    # # Trừ đi 1 để lấy số lớn nhất như trong yêu cầu
    # x -= 1
    
    print(count_p)
