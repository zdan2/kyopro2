n=int(input())
c=0
r=float('inf')
for i in range(n):
    s,t=input().split()
    if s=='Takahashi':
        t=int(t)
        if t<r:
            c=i
            r=t
print(c+1)