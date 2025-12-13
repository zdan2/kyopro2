n=int(input())
a=list(map(int,input().split()))
ca=[0]
for e in a:
    ca.append(ca[-1]+e)
c=0
for l in range(n):
    for r in range(l+1,n+1):
        s=ca[r]-ca[l]
        for i in range(l,r):
            if s%a[i]==0:
                break
        else:
            c+=1
print(c)