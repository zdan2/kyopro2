n=int(input())
a=list(map(int,input().split()))
d=[0]
for e in a:
    d.append(d[-1]+e)
for i in range(n-1):
    r=[]
    for j in range(i+1,n):
        r.append(d[j]-d[i])
    print(*r)