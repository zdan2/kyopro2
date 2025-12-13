from sortedcontainers import SortedList
l=SortedList()
l.add([10**9+1,10**9+1])
l.add([0,0])
print(l)
n,q=map(int,input().split())
for _ in range(q):
    k=list(map(int,input().split()))
    idx=l.bisect(k)-1
    d=k[1]-k[0]+1
    if l[idx][1]>=k[1]:
        print(n)
        continue
    if l[idx][1]>=k[0]:
        d-=l[idx][1]-k[0]+1
        l[idx][1]=k[1]
    if l[idx+1][0]<=k[1]:
        d-=k[1]-l[idx+1][0]+1
        l[idx+1][0]=k[0]
    if l[idx][1]>=l[idx+1][0]:
        l[idx+1][0]=l[idx][0]
        l.pop(idx)
    if l[idx][1]<k[0] and l[idx+1][0]>k[1]:
        l.add(k)
    n-=d
    print(n)