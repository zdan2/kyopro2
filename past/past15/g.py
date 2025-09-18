n,m=map(int,input().split())
a=[ [set() for _ in range(15)] for _ in range(15)]
b=[[set() for _ in range(15)] for _ in range(15)]
print(a)
for i in range(m):
    k=int(input())
    for j in range(k):
        aa,bb=map(int,input().split())
        a[i][j].add(aa)
        b[i][j].add(bb)
        
for r in a:
    print(r)
print('')
for r in b:
    print(r)
        
    