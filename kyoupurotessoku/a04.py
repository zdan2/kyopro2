from collections import defaultdict
n=int(input())
a=list(map(int,input().split()))
d=defaultdict(list)

for i,e in enumerate(a):
    d[e].append(i+1)

q=int(input())

for _ in range(q):
    l,r=map(int,input().split())
    mc=0 
    for k,v in d.items():
        if v[0]<l or v[-1]>r:
            mc=max(k,mc)
    print(mc)