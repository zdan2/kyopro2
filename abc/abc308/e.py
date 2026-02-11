n=int(input())
a=list(map(int,input().split()))
s=input()
sf={'M':[0,0,0],'ME':{(0,0):0,(0,1):0,(0,2):0,(1,1):0,(1,2):0,(2,2):0}}
c=0
for i in range(n):
    if s[i]=='M':
        sf['M'][a[i]]+=1
    if s[i]=='E':
        for j in range(3):
            k=a[i]
            l=sf['M'][j]
            if k<j:
                j,k=k,j
            sf['ME'][(j,k)]+=l
    if s[i]=='X':
        n3=a[i]
        for (n1,n2),v in sf['ME'].items():
            if v:
                u={0,1,2,3}
                for e in (n1,n2,n3):
                    u.discard(e)
                c+=min(u)*v
print(c)