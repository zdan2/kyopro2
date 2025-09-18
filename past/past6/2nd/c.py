n,m=map(int,input().split())
cp=[]
for _ in range(n):
    k=list(map(int,input().split()))
    s=set(k[1:])
    cp.append(s)
p,q=map(int,input().split())
b=set(map(int,input().split()))
c=0
for p in cp:
    if len(b&p)>=q:
        c+=1
print(c)