a,b,c,d,r=map(int,input().split())
res=set()
for i in range(c+r):
    if i==b:
        a=c
    if i%d==0:
        if i<=a:
            res.add((a,a+r))
        else:
            res.add((i,a+r))
res=sorted(res)
if res[0][0]<=c and res[0][1]>=c+r:
    print('Yes')
elif len(res)>=2 and res[1][0]<=c and res[1][1]>=c+r:
    print('Yes')
elif len(res)>=2 and res[0][1]>=res[1][0] and res[0][0]<=c and res[1][1]>=c+r:
    print('Yes')
else:
    print('No')