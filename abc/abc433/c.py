s=list(map(int,input()))+[-1]
cur=s[0]
b=[]
c=1
for e in s[1:]:
    if e==cur:
        c+=1
    else:
        b.append((cur,c))
        cur=e
        c=1
r=0
for i in range(len(b)-1):
    n1,c1=b[i]
    n2,c2=b[i+1]
    if n1+1==n2:
        r+=min(c1,c2)
print(r)