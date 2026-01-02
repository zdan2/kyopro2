n=int(input())
a=list(map(int,input().split()))

def add(bit,i,x):
    i+=1
    while i<=n:
        bit[i]+=x
        i+=i&-i

def f_sum(bit,i):
    i+=1
    a=0
    while i>0:
        a+=bit[i]
        i-=i&-i
    return a

for i in range(n):
    bit=[0]*(n+1)
    c=0
    for j,e in enumerate(a):
        add(bit,e,1)
        c+=(j+1)-f_sum(bit,e)
    print(c)
    a=a[1:]+[a[0]]