n,q=list(map(int,input().split()))
a=list(map(int,input().split()))
sa=sorted(a)
for _ in range(q):
    k=int(input())
    b=list(map(int,input().split()))
    c=sorted([a[i-1] for i in b])
    for i in range(k):
        if c[i]!=sa[i]:
            print(sa[i])
            break
    else:
        print(sa[k])