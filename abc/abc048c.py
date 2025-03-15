n,x=map(int,input().split())
a=[0]+list(map(int,input().split()))+[0]
c=0
for i in range(n+1):
    d=max(0,(a[i]+a[i+1])-x)
    a[i+1]-=d
    c+=d
print(c)
    