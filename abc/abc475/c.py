n,s,l=map(int,input().split())
a=list(map(int,input().split()))
la=[0]
for k in a[:s-1][::-1]:
    la.append(la[-1]+k)
ra=[0]
for k in a[s-1:]:
    ra.append(ra[-1]+k)
visit=0
for i,rr in enumerate(ra):
    for j,ll in enumerate(la):
        if rr*2+ll>l and ll*2+rr>l:
            break
        visit=max(visit,i+j)
print(visit+1)