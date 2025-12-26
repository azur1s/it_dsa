import json
my_list = json.loads(input())

m = 99999999.0  # m i n
n = -99999999.0 # m a x
s = 0.0

for num in my_list:
    if num < m:
        m = num
    if num > n:
        n = num
    s += num

print((n, m, round(s / len(my_list), 2)))