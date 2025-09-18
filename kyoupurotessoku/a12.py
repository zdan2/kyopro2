n,q=map(int,input().split())
l=1
r=2
c=0
for q in range(q):
    h,t=input().split()
    t=int(t)
    r=[]
    r.append((1,l))
    r.append((1,l+n))
    r.append((2,t))
    r.append((2,n+t))
    r.append((3,r))
    r.append((3,r+n))
    sr=sorted(r,key=lambda x:x[1])
    
    print(sr)
        
         
       