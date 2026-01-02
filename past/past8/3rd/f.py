n=int(input())
s=input()
idx=[]
for i in range(n):
    if s[i]=='0':
        idx.append(i)
b=[i+1 for i in idx]
if len(b)==1:
    print(-1)
    exit()
elif len(b)==0:
    print(*[i+1 for i in range(n)])
    exit()
b=b[1:]+[b[0]]
r=[i+1 for i in range(n)]
for i,e in zip(idx,b):
    r[i]=e
print(*r)