from collections import Counter
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=Counter(b)
r=[]
for i in range(n):
    if c[a[i]]:
        c[a[i]]-=1
    else:
        r.append(a[i])
print(*r)