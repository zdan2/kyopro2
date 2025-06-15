n,m=map(int,input().split())
a=[]
for _ in range(n):
    s=input()
    r={}
    for e in ('W','R','B'):
        r[e]=s.count(e)
    a.append(r)
mc=float('inf')
for i in range(1,n-1):
    for j in range(i+1,n):
        c=0
        for r in a[:i]:
            c+=m-r['W']
        for r in a[i:j]:
            c+=m-r['B']
        for r in a[j:]:
            c+=m-r['R']
        mc=min(mc,c)
print(mc)