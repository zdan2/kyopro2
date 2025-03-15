n,a,b=map(int,input().split())
d=list(map(int,input().split()))
c=sorted(set([e%(a+b) for e in d]))
lc=len(c)
if lc==1:
    print('Yes')
    exit()
c+=[e+a+b for e in c]
l=0
for r in range(1,len(c)):
    if c[r]-c[l]<a and r-l+1>=lc:
        print('Yes')
        exit()
    elif c[r]-c[l]>=a:
        while c[r]-c[l]>=a:
            l+=1
print('No')