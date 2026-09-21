n=int(input())
r=[tuple(map(int,input().split())) for _ in range(n)]
r.sort()  # 始点順

res=[]
cs,ct,cp=r[0]
for s,t,p in r[1:]:
    if s<=ct:            # 端が接するのも重なり扱いなら <=、そうでなければ 
        ct=max(ct,t)
        cp+=p
    else:
        res.append((cs,ct,cp))
        cs,ct,cp=s,t,p
res.append((cs,ct,cp))

print(res)