def d(n, m):
    return n % m == 0

def f(x, A):
    return ((d(x, 36) and d(x, 42)) <= d(x, A)) and (A * (A - 25) < 25 * (A + 200))

for A in range(1, 1001):
    flag = 0
    for x in range(1, 1001):
        if not(f(x, A)):
            flag = 1
            break
    if flag == 0:
        print(A)
