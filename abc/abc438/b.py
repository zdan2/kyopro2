def f(s,t):
    l=len(t)
    c=0
    for i in range(l):
        x=int(s[i])
        y=int(t[i])
        if x<y:
            x+=10
        c+=(x-y)
    return c
n,m=map(int,input().split())
s=input()
t=input()
r=float('inf')
for i in range(n-m+1):
    r=min(r,f(s[i:i+m],t))
print(r)