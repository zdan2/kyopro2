n=int(input())
a=list(map(int,input().split()))
pc=1
ps=a[0]
nc=0
ns=0
mod=10**9+7
for e in a[1:]:
    npc=(pc+nc)%mod
    nnc=pc
    nps=(ps+ns+e*npc)%mod
    nns=(ps-e*nnc)%mod
    pc,ps,nc,ns=npc,nps,nnc,nns
print((ps+ns)%mod)