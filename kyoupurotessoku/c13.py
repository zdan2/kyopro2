from collections import defaultdict

def get_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i*i != n:
                divisors.append(n // i)
    return sorted(divisors) 

n,p=map(int,input().split())
a=list(map(int,input().split()))
d=defaultdict(int)
mod=1000000007 
for e in a:
    b=e%mod
    d[b]+=1
print(d)
print(get_divisors(p))