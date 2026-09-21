import sys
sys.setrecursionlimit(10**9)
n,k=map(int,input().split())
r=[]
arr=[]
def f(c=0):
    m=len(arr)
    x=n-m
    if x==1:
        arr.append(k-c)
        r.append(arr[::-1])
        arr.pop()
        return
        r.append(arr+[0]*(n-m))
        return
    for i in range((k-c)//x+1):
        arr.append(i)
        f(c+i*x)
        arr.pop()
f()
for e in sorted(r):
    print(*e)