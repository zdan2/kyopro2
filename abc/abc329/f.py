n,q=map(int,input().split())
c=list(map(int,input().split()))
s=[{e} for e in c]
for _ in range(q):
    a,b=map(int,input().split())
    a-=1
    b-=1
    sa,sb=s[a],s[b]
    if len(s[a])<len(s[b]):
        sa,sb=sb,sa
    sa|=sb
    s[b]=sa
    s[a]=set()
    print(len(s[b]))