def f(can):
    can=sorted(can,key=lambda x:[-x[1],-x[2]])
    l=len(can)
    mh=can[0][0]
    mw=can[0][1]
    md=can[0][2]
    for i in range(1,l):
        h,w,d=can[i]
        if w<=mw and d<=md:
            mw=w
            md=d
            mh+=h
    return mh
        
n=int(input())
block=[]
for _ in range(n):
    h,w,d=map(int,input().split())
    block.append((h,max(w,d),min(w,d)))
mh=0
for i in range(2**n):
    can=[]
    for j in range(n):
        if i&(1<<j):
            can.append(block[j])
    if can:
        h=f(can)
        mh=max(mh,h)
print(mh)