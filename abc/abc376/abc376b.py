n,q=map(int,input().split())
l=1
r=2
c=0
for _ in range(q):
    h,t=input().split()
    t=int(t)
    a=[]
    a.append((1,l))
    a.append((1,l+n))
    a.append((2,t))
    a.append((2,n+t))
    a.append((3,r))
    a.append((3,r+n))
    sa=sorted(a,key=lambda x:x[1])
    
    for i in range(3):
        if sa[i][0]==1 and sa[i+1][0]==2:
            ip=i
            p=1
            break
        elif sa[i][0]==3 and sa[i+1][0]==2:
            ip=i
            p=2
            break
    if h=="R" and p==1:
        c += sa[ip+2][1] - sa[ip+1][1]
    elif h=="R" and p==2:
        c += sa[ip+1][1] - sa[ip][1]
    elif h=="L" and p==1:
        c += sa[ip+1][1] - sa[ip][1]
    elif h=="L" and p==2:
        c += sa[ip+2][1] - sa[ip+1][1]

    if h=="R":
        r = t
    elif h=="L":
        l = t

print(c)
