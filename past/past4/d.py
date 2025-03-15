n=int(input())
s=list(input())

lc=0
for i in range(n):
    if s[i]=='.':
        lc+=1
    else:
        break
    
rc=0
for j in range(n-1,-1,-1):
    if s[j]=='.':
        rc+=1
    else:
        break

mc=0
c=0
for k in range(i,j+1):
    if s[k]=='.':
       c+=1
    else:
        mc=max(mc,c)
        c=0
mc=max(mc,c)

if lc>=rc:
    cc=mc-lc
    if cc>rc:
        print(lc,cc)
    else:
        print(lc,rc)
else:
    cc=mc-rc
    if cc>lc:
        print(cc,rc)
    else:
        print(lc,rc)

