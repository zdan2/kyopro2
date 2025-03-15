from collections import Counter
n,m,k=map(int,input().split())
mx=[input() for _ in range(n)]

for l in range(min(n,m),0,-1):
    r=''
    for i in range(n-l+1):
        for j in range(m-l+1):
            r=''.join(mx[i+x][j:l+j] for x in range(l))
            c=Counter(r).most_common()[0][1]
            if l*l-c<=k:
                print(l)
                exit()
            

        