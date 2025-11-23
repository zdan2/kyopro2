def sort(arr):
    if len(arr)==1:
        return arr
    if not arr:
        return []
    
    n=len(arr)
    l=sort(arr[:n//2])
    r=sort(arr[n//2:])
    return merge(l,r)

def merge(l,r):
    ll=len(l)
    lr=len(r)
    li=0
    ri=0
    res=[]
    while li<ll and ri<lr:
        if l[li]<r[ri]:
            res.append(l[li])
            li+=1
        else:
            res.append(r[ri])
            ri+=1
    if li<ll:
        for i in range(li,ll):
            res.append(l[i])
    if ri<lr:
        for i in range(ri,lr):
            res.append(r[i])
    return res

n=int(input())
arr=list(map(int,input().split()))
print(*sort(arr))