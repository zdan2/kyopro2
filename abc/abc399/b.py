n=int(input())
p=list(map(int,input().split()))
l=[0]*(n)
r=1
s=sorted(set(p),reverse=True)
for e in s:
    c=0
    for i in range(n):
        if p[i]==e:
            l[i]=r
            c+=1
    r+=c
for a in l:
    print(a)
