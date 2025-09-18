n,k=map(int,input().split())
a=list(map(int,input().split()))
r=1
for e in a:
    r*=e
    if r>=10**k:
        r=1
print(r)