n,k=map(int,input().split())
s=list(input())
p=s[0]
c=0
for e in s[1:]:
    if e==p:
        continue
    p=e
    c+=1
print(n-1-max(c-2*k,0))