n,q=map(int,input().split())
x=list(map(int,input().split()))
b=[0]*n
for i,e in enumerate(x):
    if e!=0:
        b[e-1]+=1
    else:
        j=b.index(min(b))
        b[j]+=1
        x[i]=j+1
print(*x)