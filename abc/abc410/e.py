import heapq
n,m,h=map(int,input().split())
hq=[(-(m+h),m,h,0)]
heapq.heapify(hq)
c=0
mdm=0
for _ in range(n):
    a,b=map(int,input().split())
    ns={}
    while hq:
        _,cm,ch,dm=heapq.heappop(hq)
        mdm=max(mdm,dm)
        if cm>=a:
            ncm,nch,ndm=cm-a,ch,dm+1
            if (ncm,nch) not in ns or ndm>ns[(ncm,nch)]:
                ns[(ncm,nch)]=ndm
        if ch>=b:
            ncm,nch,ndm=cm,ch-b,dm+1
            if (ncm,nch) not in ns or ndm>ns[(ncm,nch)]:
                ns[(ncm,nch)]=ndm
    for k,v in ns.items():
        heapq.heappush(hq,(-(k[0]+k[1]),k[0],k[1],v))
if hq:
    mdm+=1
print(mdm)     