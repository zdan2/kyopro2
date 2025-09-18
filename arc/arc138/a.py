from bisect import bisect,bisect_left
n,k=map(int,input().split())
a=list(map(int,input().split()))
ak=a[:k]
an=a[k:]
sak=min(ak)
san=min(an)
print(ak,an)
aki=sorted([(e,i) for i,e in enumerate(ak)])
ani=sorted([(e,i) for i,e in enumerate(an)])
print(aki,ani)
idx1=bisect(aki,san)
idx2=bisect_left(ani,sak)
print(idx1,idx2)