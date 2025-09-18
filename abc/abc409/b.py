from bisect import bisect_left
n=int(input())
a=list(map(int,input().split()))
a.sort()
for i in range(n,-1,-1):
    if i<=n-bisect_left(a,i):
        print(i)
        break