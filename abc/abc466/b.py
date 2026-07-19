n,m=map(int,input().split())
d=[-1]*m
for _ in range(n):
    c,s=map(int,input().split())
    c-=1
    d[c]=max(d[c],s)
print(*d)