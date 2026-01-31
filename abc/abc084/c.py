n=int(input())
q=[tuple(map(int,input().split())) for _ in range(n-1)]
for i in range(n-1):
    now=0
    for c,s,f in q[i:]:
        
        now+=max(s-now,s+(now-s+f-1)//f*f)
        now+=c
        
        
    
    