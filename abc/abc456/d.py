d={'a':0,'b':0,'c':0}
mod=998244353
s=input()
for e in s:
    d[e]+=1
    for k,v in d.items():
        if k!=e:
            d[e]=(d[e]+v)%mod
print(sum(d.values())%mod)