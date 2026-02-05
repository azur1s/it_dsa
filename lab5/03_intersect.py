import json

def isIntersect(a, b, c):
    return bool(set(a) & set(b) & set(c))

a = json.loads(input())
b = json.loads(input())
c = json.loads(input())

print(isIntersect(a, b, c))