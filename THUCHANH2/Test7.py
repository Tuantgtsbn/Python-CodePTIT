# def check(b):
#     for i in a:
#         if int(i/b) == int(i/(b+1)):
#             return False
#     return True

# n = int(input())
# a = [int(i) for i in input().split()]
# s, ans = min(a), 0
# for i in range(s,0,-1):
#     if check(i):
#         for j in range(n):
#             ans += int(a[j]/(i+1)) + 1
#         break
# print(ans)
class SV:
    def __init__(self):
        self.n=19
        pass
def change(sv):
    sv.n+=1
sv=SV()
change(sv)
print(sv.n)
