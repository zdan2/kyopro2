n,k=map(int,input().split())
s=list(map(int,input().split()))
for i in range(n):
    if s[i]==0:
        break
l=min(k,i)
for i in range(n-1,-1,-1):
    if s[i]==0:
        break
r=max(i+1,k)
c=s[l:r]
print(len(c)+c.count(1))