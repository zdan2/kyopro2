t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a.sort()
    b.sort(reverse=True)
    i=0
    j=0
    c=0
    while i<n:
        if b[j]>=m-a[i]:
            c+=1
            j+=1
            i+=1
        else:
            i+=1
    print(sum(a)+sum(b)-c*m) 