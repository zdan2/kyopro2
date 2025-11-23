n,w=map(int,input().split())
a=list(map(int,input().split()))
c=sum(a[:w])
r=c
for i in range(w,n):
    c-=a[i-w]
    c+=a[i]
    r=max(r,c)
print(r)