n,m=map(int,input().split())
mmx=-float('inf')
mix=float('inf')
mmy=-float('inf')
miy=float('inf')
r=[]
for _ in range(n):
    a,b=map(int,input().split())
    x=a-b
    y=a+b
    mmx=max(mmx,x)
    mix=min(mix,x)
    mmy=max(mmy,y)
    miy=min(miy,y)
    r.append((x,y))
for _ in range(m):
    p=int(input())-1
    x,y=r[p]
    print(max((max(abs(mmx-x),abs(mix-x)),max(abs(mmy-y),abs(miy-y)))))
    