from bisect import bisect_left,bisect
n,q=map(int,input().split())
a=sorted(map(int,input().split()))
ca=[0]
for e in a:
    ca.append(ca[-1]+e)
for _ in range(q):
    b=int(input())
    if b>a[-1]:
        print(-1)
        continue
    if b==1:
        print(1)
        continue
    l=bisect(a,b-1)
    c=ca[l]
    c+=(n-l)*(b-1)+1
    print(c)