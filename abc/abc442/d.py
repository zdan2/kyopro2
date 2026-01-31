n,q=map(int,input().split())
a=list(map(int,input().split()))
ca=[0]
for e in a:
    ca.append(ca[-1]+e)
for _ in range(q):
    x=list(map(int,input().split()))
    if x[0]==1:
        i=x[1]-1
        j=i+1
        if a[i]<=a[j]:
            ca[i+1]+=a[j]-a[i]
        else:
            ca[i+1]-=a[i]-a[j]
        a[i],a[j]=a[j],a[i]
    else:
        l=x[1]-1
        r=x[2]
        print(ca[r]-ca[l])