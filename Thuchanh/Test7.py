def count_pivots(arr):
    n = len(arr)
    left_max = [0] * n
    right_min = [0] * n

    left_max[0] = arr[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], arr[i])

    right_min[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        right_min[i] = min(right_min[i + 1], arr[i])

    pivot_count = 0
    for i in range(n):
        if left_max[i] == arr[i] and right_min[i] == arr[i]:
            pivot_count += 1

    return pivot_count

# Đọc số lượng bộ test
T = int(input())

for i in range(T):
    # Đọc số lượng phần tử của dãy số
    N = int(input())
    
    # Đọc dãy số A[]
    A = list(map(int, input().split()))
    
    # Tính và in ra số lượng phần tử chốt trong dãy số A[]
    pivot_count = count_pivots(A)
    print(pivot_count)
