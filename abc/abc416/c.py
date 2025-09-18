def f(num,k):
    if num<k:
        return str(num)
    return f(num//k,k)+str(num%k)

n,k,x=map(int,input().split())
d=[]
for _ in range(n):
    d.append(input())
d.sort()
a=[]
for i in range(n**k):
    s=f(i,n)
    s='0'*(k-len(s))+s
    r=''
    for e in list(s):
        r+=d[int(e)]
    a.append(r)
a.sort()
print(a[x-1])