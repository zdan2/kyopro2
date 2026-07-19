
n,d=map(int,input().split())
m=[0]*(10**6+1)
for _ in range(n):
    s,t=map(int,input().split())
    if t-s<d:
        continue
    m[s]+=1
    m[t-d+1]-=1
c=0
r=0
for i in range(len(m)):
    c+=m[i]
    r+=c*(c-1)//2
print(r)