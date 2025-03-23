n,m=map(int,input().split())
r=[0]
for _ in range(n-1):
    r.append(r[-1]+int(input()))
d=0
now=0
for _ in range(m):
    nxt=now+int(input())
    s=min(nxt,now)
    g=max(nxt,now)
    d+=r[g]-r[s]
    d%=100000
    now=nxt
print(d)