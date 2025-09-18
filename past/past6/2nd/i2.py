from bisect import bisect_left
h,w=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(h)]
res=[0]
for i in range(h):
    for j in range(w):
        idx=bisect_left(res,a[i][j])
        if idx==len(res):
            res.append(a[i][j])
        else:
            res[idx]=a[i][j]
print(res)