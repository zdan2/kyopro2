n,l,r=map(int,input().split())
c=0
for _ in range(n):
    x,y=map(int,input().split())
    if x<=l and r<=y:
        c+=1
print(c)