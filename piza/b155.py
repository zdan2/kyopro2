h,w,n=map(int,input().split())
stamp=[]
for i in range(n):
    c=[]
    for i in range(h):
        c.append(input())
    stamp.append(c)
row,collumn =map(int,input().split())
mx=[list(map(int,input().split())) for _ in range(row)]
    
for e in mx:
    r = [stamp[i-1] for i in e]
    for line_idx in range(h):
        line = ""
        for st in r:
            line += st[line_idx]
        print(line)
        
        
        