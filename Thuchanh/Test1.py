def max_product(N, A):
    A.sort()
    
    # Tích của 2 số lớn nhất
    max_product_2 = A[-1] * A[-2]

    # Tìm tích của 2 số âm nhỏ nhất và số dương lớn nhất (nếu có)
    max_product_2_negatives = A[0] * A[1] * A[-1]

    # Tích của 3 số dương lớn nhất (nếu có)
    max_product_3 = A[-1] * A[-2] * A[-3]

    # Trả về giá trị lớn nhất trong các trường hợp trên
    return max(max_product_2, max_product_2_negatives, max_product_3)

# Đọc số lượng phần tử của dãy
N = int(input())

# Đọc dãy số A
A = list(map(int, input().split()))

# Tính và in ra kết quả
result = max_product(N, A)
print(result)
