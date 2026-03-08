n,c=map(int,input().split())
a=list(map(int,input().split()))
for e in a:
    if e<c:
        print(1)
        c=e
    else:
        print(0)