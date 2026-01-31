import math
n,k = map(int, input().split())
b=2*n-1
a=(math.isqrt(b*b+8*k)-b)//2
if a<0:
    a=0
def D(x):
    return (x+1)*n+x*(x+1)//2
while D(a) < k:
    a += 1
while a > 0 and D(a-1) >= k:
    a -= 1
print(a)