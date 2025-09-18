h,w=map(int,input().split())
mx=[list(input()) for _ in range(h)]
tx=[r for r in zip(*mx[::-1])]
mc=0
c=0
for r in tx:
    if r[0]=='1':
        c+=r.count('1')
    else:
        mc=max(mc,c)
        c=0
mc=max(mc,c)
print(mc)