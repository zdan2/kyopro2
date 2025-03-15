r=[True]*1000001
r[0]=False
r[1]=False
for i in range(2,1000001):
    if r[i]==True:
        for j in range(i+i,1000001,i):
            r[j]=False
p=[i for i,v in enumerate(r) if v]

n=int(input())
rn=int((n)**0.5)
c = 0
m = len(p)
for i in range(m):
    if p[i]*p[i] > rn:
        break
    for j in range(i+1, m):
        if (p[i]*p[j])**2 <= n:
            c += 1
        else:
            break

print(c)
    
