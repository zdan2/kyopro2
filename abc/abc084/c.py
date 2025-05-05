n=int(input())
t=[list(map(int,input().split())) for _ in range(n)]
r=[]
for i in range(n-2):
    pc,ps,pf=t[i]
    time=ps
    for c,s,f in t[i:]:
        time+=pc
        if time<=s:
            time=s
        else:
            time=s+f*(time-s+f-1)//f
        r.append(time)
        pc,ps,pf=c,s,f
print(time)        
        
        
    
    