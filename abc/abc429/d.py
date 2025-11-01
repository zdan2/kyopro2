from collections import Counter
n,m,cc=map(int,input().split())
a=list(map(int,input().split()))
ro=cc//n
rem=cc%n
c=sorted(Counter(a).most_common())
le=len(c)
c+=[(c[i][0]+m,c[i][1]) for i in range(le)]
ca=[c[0]]
for i in range(1,len(c)):
    ca.append((c[i][0],ca[-1][1]+c[i][1]))
r=1
res=ro*m*n
if rem==0:
    print(res)
    exit()
for l in range(le):
    r=max(r,l+1)
    while ca[r][1]-ca[l][1]<rem:
        r+=1
    iv=ca[l+1][0]-ca[l][0]
    met=ca[r][1]-ca[l][1]
    res+=iv*met
print(res)