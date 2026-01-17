from collections import defaultdict
n=int(input())
a=list(map(int,input().split()))
d=defaultdict(list)
for i in range(n):
    d[a[i]].append((i+1))
e=defaultdict(lambda:0)
print(d)
for k,v in d.items():
    print(e)
    if len(v)<=1:
        continue
    pre=v[0]
    for nxt in v[1:]:
        print(k,nxt,pre)
        e[k]*=2
        e[k]+=(nxt-pre-1)
        pre=nxt
print(e)