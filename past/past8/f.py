n=int(input())
s=list(input())
c0=s.count('0')
if c0==1:
    print(-1)
    exit()
r=[]
idx=[]
for i in range(n):
    if s[i]=='1':
        r.append(i+1)
    else:
        r.append(0)
        idx.append(i+1)

for i in range(n):
    if r[i]==0:
        if idx[-1]!=i+1:
            r[i]=idx.pop()
        else:
            r[i]=idx.pop(0)
        

print(*r)


    
