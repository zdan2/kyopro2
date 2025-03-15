from itertools import product

n,m=map(int,input().split())
p=list(product([0,1],repeat=n))
s=[tuple(map(int,input().split())) for _ in range(m)]
s=[(a-1,b-1,c-1) for a,b,c in s]
mc=0
for pr in p:
    c1,c2,c3=0,0,0
    for a,b,c in s:
        print(a,b,c)
        print(pr)
        if pr[a]==1 and pr[b]==1 and pr[c]==1:
            break
        else:
            for a,b,c in s:
                if pr[a]==1 and pr[b]==1:
                    c1+=1
                elif pr[a]==1 and pr[c]==1:
                    c2+=1
                elif pr[b]==1 and pr[c]==1:
                    c3+=1
    else:
        mc=max(c1,c2,c3,mc)
print(mc)
        
    
