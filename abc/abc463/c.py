n=int(input())
s=[list(map(int,input().split())) for _ in range(n)]
s=sorted(s)
q=int(input())
t=[(e,i) for i,e in enumerate(map(int,input().split()))]
t.sort()
r=[0]*q
for e,i in t:
    while s[-1][1]<=e:
        s.pop()
    r[i]=s[-1][0]
for e in r:
    print(e)