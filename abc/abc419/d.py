n,m=map(int,input().split())
s=input()
t=input()
a=[0]*(n+1)
for _ in range(m):
    l,r=map(int,input().split())
    a[l-1]+=1
    a[r]-=1
ca=[a[0]]
for i in range(1,n+1):
    ca.append(ca[-1]+a[i])
ca=[i%2 for i in ca]
t=[s[i] if e==0 else t[i] for i,e in enumerate(ca[:n])]
print(''.join(t))