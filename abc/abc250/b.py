n,a,b=map(int,input().split())
wh='.'*b
bl='#'*b
r1=[''.join(wh if i%2==0 else bl for i in range(n))]*a
r2=[''.join(bl if i%2==0 else wh for i in range(n))]*a
for i in range(n):
    c=r1 if i%2==0 else r2
    for r in c:
        print(r)