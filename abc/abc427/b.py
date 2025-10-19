def f(n):
    r=0
    while n>0:
        r+=n%10
        n//=10
    return r
n=int(input())
a=1
for _ in range(n-1):
    a+=f(a)
print(a)