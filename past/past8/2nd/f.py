n=int(input())
s=input()
r=[0]*n
v=[]
for i in range(n):
    if s[i]=='1':
        r[i]=i+1
    else:
        v.append(i+1)
if len(v)==1:
    print(-1)
    exit()
else:
    v=v[1:]+v[:1]
    v=v[::-1]
    for i,e in enumerate(r):
        if e==0:
            r[i]=v.pop()
print(*r)        

        