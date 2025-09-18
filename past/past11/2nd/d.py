
def fd(x,d):
    if d[x]!=x:
        d[x]=fd(d[x],d)
    return d[x]
d=[-1]*26
n=int(input())
for _ in range(n):
    a,b=input().split()
    a=ord(a)-ord('a')
    b=ord(b)-ord('a')
    if d[a] ==-1 and d[b]==-1:
        d[min(a,b)]=min(a,b)
        d[max(a,b)]=min(a,b)
    elif d[a]==-1:
        d[a]=fd(b,d)
    elif d[b]==-1:
        d[b]=fd(a,d)
    else:
        x=fd(a,d)
        y=fd(b,d)
        if x!=y:
            d[x]=y
def f(s):
    for l in range(len(s)):
        i=ord(s[l])-ord('a')
        if d[i]!=-1:
            root=fd(d[i],d)
            s[l]=chr(ord('a')+root)
    return s
rs=f(list(input()))
rt=f(list(input()))
print('Yes' if rs==rt else 'No')