n,k=map(int,input().split())
a=[int(input()) for _ in range(n)]+[float('inf')]
if 0 in a:
    print(len(a)-1)
    exit()
if k==0:
    print(0)
    exit()
l=0
cur=1
ml=0
for r in range(n+1):
    cur*=a[r]
    if cur<=k:
        continue
    ml=max(ml,r-l)
    while cur>k:
        cur//=a[l]
        l+=1
print(ml)