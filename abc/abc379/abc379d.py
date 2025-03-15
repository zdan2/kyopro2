from collections import defaultdict
n=int(input())
d=defaultdict(int)

for _ in range(n):
    q=list(map(int,input().split()))
    if q[0]==1:
        d[0]+=1
    elif q[0]==2:
        nd=defaultdict(int)
        for k,v in d.items():
            nd[k+q[1]]+=v
        d=nd
    elif q[0]==3:
        r=[]
        v=0
        for k in list(d.keys()):
            if k>=q[1]:
                v+=d.pop(k)
        print(v)
            
                
              