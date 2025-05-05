n,m,k,q=map(int,input().split())
can=[]
wocan=[]
for _ in range(n):
    p,t=map(int,input().split())
    if t==1:
        can.append(p)
    else:
        wocan.append(p)
can.sort()
wocan.sort()
ac=[0]
for e in can:
    ac.append(ac[-1]+e)
aw=[0]
for e in wocan:
    aw.append(aw[-1]+e)
mc=float('inf')
for i in range(len(ac)):
    if 0<=m-i<len(aw):
        mc=min(mc,ac[i]+(i+k-1)//k*q+aw[m-i])
print(mc)