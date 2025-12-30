import math

def f(n, a, b):
    if b>n:
        return 0
    B=2*b-a
    D=B**2+8*a*n
    numerator=-B+math.isqrt(D) 
    r=numerator//(2*a)
    return r

n=int(input())
for _ in range(n):
    n,a,b=map(int,input().split())
    print(f(n,a,b))