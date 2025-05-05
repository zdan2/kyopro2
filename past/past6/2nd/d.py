from itertools import accumulate
n,k=map(int,input().split())
a=list(map(int,input().split()))
c=[0]+list(accumulate(a))
for i in range(n-k+1):
    print(c[k+i]-c[i])