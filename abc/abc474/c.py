n,q=map(int,input().split())
p=list(map(int,input().split()))
cur_last=n
d={e:i for i,e in enumerate(p)}
for _ in range(q):
    a=int(input())
    d[a]=cur_last
    cur_last+=1
l=[(v,k) for k,v in d.items()]
l.sort()
r=[k for v,k in l]
print(*r)