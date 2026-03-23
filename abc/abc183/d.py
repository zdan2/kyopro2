import sys
sys.setrecursionlimit(10**6)
from functools import cache
@cache
def f(a, b, c):
    if a == 100 or b == 100 or c == 100:
        return 0.0
    total = a + b + c
    e = 1.0
    e += f(a + 1, b, c) * (a / total)
    e += f(a, b + 1, c) * (b / total)
    e += f(a, b, c + 1) * (c / total)
    return e
a, b, c = map(int, input().split())
print(f(a, b, c))