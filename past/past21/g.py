n,k=map(int,input().split())
c=sorted([list(map(int,input().split()))+[i+1] for i in range(n)])
r=[]
for i in range(n-1):
    x,y,z=c[i]
    o,p,q=c[i+1]
    if o<x+y*k:
        r.append(z)
print(len(r))
print(*sorted(r))