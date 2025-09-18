r,n,m,l=map(int,input().split())
s=list(map(int,input().split()))
c=0
cm=m
cr=0
for i in range(l):
    cm-=1
    c+=s[i]
    if c==n:
        cm=m
        c=0
        cr+=1
    if c>n:
        print('No')
        exit()
    if cm==0:
        cm=m
        c=0
        cr+=1
if cm==m and cr==r:
    print('Yes')
else:
    print('No')
    
            