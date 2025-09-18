a=list(map(int,input().split()))
b=['A','B','C','D','E']
r=[]
for i in range(1,32):
    c=0
    d=''
    for j in range(5):
        if (i>>j)&1:
           c+=a[j]
           d+=b[j]
    r.append((c,d))
r=sorted(r,key=lambda x:[-x[0],x[1]])
for _,e in r:
    print(e)