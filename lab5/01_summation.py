def summation_1(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print(summation_1(int(input())))