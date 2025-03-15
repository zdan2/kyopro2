from math import gcd

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]
3
n=int(input())
a=list(map(int,input().split()))
g=abs(a[0]-a[1])

for i in range(1,n):
    g=gcd(g,abs(a[i]-a[i-1]))
s=make_divisors(g)

print(1 if len(s)!=1 else 2)
    
    