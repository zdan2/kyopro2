import math
n=int(input())
m=math.isqrt(n-1)
d=n-(m*m+1)
a=m+1-d
if a>0:
    print(a)
else:
    print(abs(a)+2)