from collections import Counter
n,m,cc=map(int,input().split())
a=list(map(int,input().split()))
ro=cc//n
rem=cc%n
c=sorted(Counter(a).most_common())
l=len(c)
c+=[(c[i][0]+m,c[i][1]) for i in range(l)]
ca=[c[0]]
for i in range(1,len(c)):
    ca.append((c[i][0],ca[-1][1]+c[i][1]))
r=1
res=ro*n
print(rem,ca)
for l in range(l+1):
    while True:
        print(l,r,res)
        if ca[r][1]-ca[l][1]<rem:
            r+=1
        else:
            res+=(ca[r][0]-ca[l][0])
            if r<=l:
                r+=1
            break
    
print(res)