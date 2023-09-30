# a,b,c=[int(x) for x in input().split()]
# def solve(n,m):
#     s=""
#     while(n!=0):
#         s+=str(n%m)
#         n//=m
#     if(s==s[::-1]):
#         return True
#     else:
#         return False

# cnt=0
# for i in range(a,b+1,1):
#     if(solve(i,c)):
#         cnt+=1
# print(cnt)
# def is_palindrome(x_str):
#     return x_str == x_str[::-1]

# def count_palindromic_numbers(a, b, M):
#     count = 0
#     for num in range(a, b + 1):
#         is_palindromic_in_all_bases = True
#         for base in range(2, M + 1):
#             num_in_base = ""
#             temp_num = num
#             while temp_num > 0:
#                 num_in_base += str(temp_num % base)
#                 temp_num //= base
#             if not is_palindrome(num_in_base):
#                 is_palindromic_in_all_bases = False
#                 break
#         if is_palindromic_in_all_bases:
#             count += 1
#     return count

# # Đọc đoạn [a, b] và số M từ input
# a, b, M = map(int, input().split())

# # Tính và in ra kết quả
# result = count_palindromic_numbers(a, b, M)
# print(result)
import math

def is_palindrome(x_str):
    return x_str == x_str[::-1]

def max_palindromic_product(a, b, M):
    if a > b:
        return 0
    
    max_palindrome_product = 0
    
    # Tìm tất cả các cơ số từ 2 đến sqrt(b)
    for base in range(2, int(math.sqrt(b)) + 1):
        num = b
        num_in_base = ""
        
        # Chuyển đổi số b sang cơ số base
        while num > 0:
            num_in_base += str(num % base)
            num //= base
        
        # Kiểm tra tính thuận nghịch trong cơ số base
        if is_palindrome(num_in_base):
            max_palindrome_product = max(max_palindrome_product, b)
    
    # Tính tích của các số còn lại trong cơ số b
    num = b
    num_in_base = ""
    while num > 0:
        num_in_base += str(num % M)
        num //= M
    
    if is_palindrome(num_in_base):
        max_palindrome_product = max(max_palindrome_product, b)
    
    return max_palindrome_product

# Đọc đoạn [a, b] và số M từ input
a, b, M = map(int, input().split())

# Tính và in ra kết quả
result = max_palindromic_product(a, b, M)
print(result)
