n=int(input())
a=list(map(int,input().split()))
r=[]
for i in range(n):
    for j in range(i,n):
        b=sorted(a[i:j+1])
        if (j-i)%2==1:
            mid1=(j-i)//2
            mid2=(j-i)//2+1
            if (b[mid1]+b[mid2])%2==0:
                r.append((b[mid1]+b[mid2])//2)
            else:
                r.append((b[mid1]+b[mid2])/2)
        else:
            mid=(j-i)//2
            r.append(b[mid])
r.sort()
if len(r)%2==0:
    mid1=len(r)//2-1
    mid2=len(r)//2
    if (r[mid1]+r[mid2])%2==0:
        res=(r[mid1]+r[mid2])//2
    else:
        res=(r[mid1]+r[mid2])/2
else:
    mid=len(r)//2
    res=r[mid]
print(res)