h,w=map(int,input().split())
g=[list(input()) for _ in range(h)]
c=0
for h1 in range(h):
    for h2 in range(h1,h):
        for w1 in range(w):
            for w2 in range(w1,w):
                d=[]
                t=[]
                for i in range(h1,h2+1):
                        d.append(g[i][w1:w2+1])
                        t.append(g[i][w1:w2+1][::-1])
                if d==t[::-1]:
                    c+=1
print(c)                