n=int(input())
a=[tuple(map(int,input().split())) for _ in range(n)]
a.sort(key=lambda x:x[1])
c=1
cur=a[0][1]
for l,r in a[1:]:
    if l>=cur:
        c+=1
        cur=r
print(c)