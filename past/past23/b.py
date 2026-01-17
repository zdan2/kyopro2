a,b,c=map(int,input().split())
if c>0:
    a,b=min(a,b),max(a,b)
    c='+'+str(c)
else:
    a,b=max(a,b),min(a,b)
print(f'{a} -> {b} ({c})')