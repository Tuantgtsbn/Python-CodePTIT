d = [0] * 15
n = 0
def Try(s) :
    if len(s) == n :
        print(s, end = ' ')
        return
    for i in range(n, 0, -1) :
        if d[i] == 0 :
            d[i] = 1
            Try(s + str(i))
            d[i] = 0

t = int(input())
for i in range(t) :
    n = int(input())
    s = 1
    for i in range(n) : s *= i + 1
    print(s)
    Try('')
    print()