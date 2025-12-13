n,m=map(int,input().split())

res=[]
def f(x,c=None):
    if c is None:
        c=[x]
    if len(c)==n:
        res.append(c)
        return
    for i in range