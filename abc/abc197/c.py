n=int(input())
a=list(map(int,input().split()))
c=float('inf')
for i in range(2**n):
    s=0
    r=0
    for j in range(n):
        if i&(1<<j):
            x=0
            for e in a[s:j]:
                x|=e
            r^=x
            s=j
    x=0
    for e in a[s:]:
       x|=e
    r^=x 
    c=min(c,r)
print(c)