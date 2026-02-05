# Problem 134 from PSCP
n = int(input())

if n == 1:
    print(1)
else:
    D = 1
    P = 1
    S = 0
    while True:
        START = P
        end = min(n, P * 10 - 1)
        if end < START:
            break
        S += (end - START + 1) * D
        if end == n:
            break
        D += 1
        P *= 10
    print(S + n)