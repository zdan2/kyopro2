t,x=map(int,input().split())
a=list(map(int,input().split()))
m=[0]
r=[a[0]]
for i in range(1,t+1):
    if abs(a[i]-r[-1])>=x:
        r.append(a[i])
        m.append(i)
for i,j in zip(m,r):
    print(i,j)