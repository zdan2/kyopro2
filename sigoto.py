from bisect import bisect
n=int(input())
point=[0]
end_idx=[0]
work=[tuple(map(int,input().split())) for _ in range(n)]
work=sorted(work,key=lambda x:x[1])
for s,t,p in work:
    idx=bisect(end_idx,s)-1
    if idx==len(point):
        point.append(p)
        end_idx.append(t)
    else:
        point.append(point[idx]+p)
        end_idx.append(t)
print(max(point))