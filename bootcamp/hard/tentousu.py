n=int(input())
a=list(map(int,input().split()))
bit=[0]*(n+1)

def add(i,x):
    i+=1
    while i<=n:
        bit[i]+=x
        i+=i&-i

def f_sum(i):
    i+=1
    a=0
    while i>0:
        a+=bit[i]
        i-=i&-i
    return a

r=0
for i,e in enumerate(a):
    add(e,1)
    r+=i-f_sum(e-1)
print(r)