from collections import defaultdict
h,w,k=map(int,input().split())
s=[list(input()) for _ in range(h)]
mx=[[0]*(w+1) for _ in range(h+1)]
for i in range(h):
    for j in range(w):
            mx[i+1][j+1]=(mx[i+1][j]+mx[i][j+1]-mx[i][j]+(1 if s[i][j]=='1' else 0))
total = 0
for u in range(h):
    mxu=mx[u]
    for b in range(u+1, h+1):
        mxb=mx[b]
        cur=[x-y for x,y in zip(mxb,mxu)] 
        a=bb=0
        for r in range(w+1):
            t=cur[r]-k
            while bb<r and cur[bb]<=t:
                bb+= 1
            while a<r and cur[a]<t:
                a+=1
            total+=bb-a
print(total)
