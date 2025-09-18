n=int(input())
a=list(map(int,input().split()))
h=(1 if a[1]>a[0] else -1)
idx=[(0,h)]
for i in range(1,n-1):
    if h==1 and a[i+1]>a[i]:
        continue
    if h==-1 and a[i+1]<a[i]:
        continue
    h*=-1
    idx.append((i,h))
idx.append((n-1,h*-1))
c=0
for i in range(1,len(idx)-2):
    if idx[i-1][1]==1:
        c1=idx[i][0]-idx[i-1][0]
        c2=idx[i+2][0]-idx[i+1][0]
        c+=c1*c2
print(c)            