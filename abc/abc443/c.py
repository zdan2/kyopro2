n,t=map(int,input().split())
a=list(map(int,input().split()))+[t]
cur=0
total=0
for e in a:
    if e<cur:
        continue
    total+=e-cur
    cur=e+100
print(total)