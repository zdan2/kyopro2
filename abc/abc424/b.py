n,m,k=map(int,input().split())
d=[0]*(n+1)
r=[]
for _ in range(k):
    a,b=map(int,input().split())
    d[a]+=1
    if d[a]==m:
        r.append(a)
print(*r)