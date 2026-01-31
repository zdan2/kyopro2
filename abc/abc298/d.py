from collections import deque
mod=998244353
q=int(input())
a=1
dq=deque([1])
for _ in range(q):
    x=list(map(int,input().split()))
    if x[0]==1:
        a=(a*10+x[1])%mod
        dq.append(x[1])
    if x[0]==2:
        y=dq.popleft()
        a=(a-y*pow(10,len(dq),mod))%mod
    if x[0]==3:
        print(a%mod)