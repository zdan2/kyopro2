n=int(input())
a=list(map(int,input().split()))
l=a[:n//2]
r=[0]+a[n//2:]
c=0
rm=r.pop()
while l and r:
    lm=l.pop()
    if lm*2<=rm:
        c+=1
        rm=r.pop()
print(c)