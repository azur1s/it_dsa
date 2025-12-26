def is_even(n):
    # last bit is 1 therefore odd number will have 1 as last bit
    # 11 = ... 1 0 1 1
    # 12 = ... 1 1 0 0
    # 13 = ... 1 1 0 1
    return (n & 1) == 0

print(is_even(int(input())))