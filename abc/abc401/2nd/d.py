n,k=map(int,input().split())
s=list(input())
for i in range(n-1):
    if s[i]=='?' and s[i+1]=='o':
        s[i]='.'
for i in range(n-1,0,-1):
    if s[i]=='?' and s[i-1]=='o':
        s[i]='.'
c=0
m=0
r=[]
for i in range(n):
    if s[i]=='?':
        c+=1
        id=i
    else:
        m+=(c+1)//2
        if c%2==1:
            r.append(id)
        c=0
if c>0:
    m+=(c+1)//2
    if c%2==1:
        r.append(id)
print(''.join(s))
print(m)
print(r)