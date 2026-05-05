r=[]
def f(n,s=''):
    if n==0:
        r.append(s)
        return
    for e in ['a','b','c']:
        f(n-1,s+e)
n=int(input())
f(n)
for e in r:
    print(e)