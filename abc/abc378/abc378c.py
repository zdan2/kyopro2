from collections import defaultdict
n=int(input())
a=list(map(int,input().split()))
d=defaultdict(int)
s=set()
b=[]
for i in range(n):
    if a[i] not in s:    
        b.append(-1)
        d[a[i]]=i+1
        s.add(a[i])
    else:
        b.append(d[a[i]])
        d[a[i]]=i+1
print(*b)