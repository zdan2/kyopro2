n,q=map(int,input().split())
a=list(map(int,input().split()))
bw=[False]*(n+2)
c=0
for e in a:
    if bw[e]:
        if bw[e-1]==False and bw[e+1]==False:
            c-=1
        if bw[e-1]==True and bw[e+1]==True:
            c+=1
        bw[e]=False
    elif not bw[e]:
        if bw[e-1]==False and bw[e+1]==False:
            c+=1
        if bw[e-1]==True and bw[e+1]==True:
            c-=1
        bw[e]=True
    print(c)