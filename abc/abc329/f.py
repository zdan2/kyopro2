n,q=map(int,input().split())
c=list(map(int,input().split()))
box=[{e} for e in c]
for _ in range(q):
    a,b=map(int,input().split())
    if len(box[a-1])>len(box[b-1]):
        box[a-1]|=box[b-1]
        box[b-1]=box[a-1]
        box[a-1]=set()
    else:
        box[b-1]|=box[a-1]
        box[a-1]=set()
    print(len(box[b-1]))