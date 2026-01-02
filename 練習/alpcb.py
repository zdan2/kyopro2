n,m=map(int,input().split())

bit=[0]*(n+1)

def add(i,x):
    while i<=n:
        bit[i] += x
        i += i & -i

def f_sum(i):
    a=0
    while i>0:
        a += bit[i]
        i -= i & -i
    return a

for i,e in enumerate(list(map(int,input().split()))):
    add(i+1,e)

for _ in range(m):
    q,a,b=map(int,input().split())
    if q==0:
        add(a+1,b)
    else:
        print(f_sum(b)-f_sum(a))
        