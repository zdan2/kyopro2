#nums=list(map(int,input().split()))
nums = [1,2,3]
ln=len(nums)
res=[]
def dfs(i,r=None,h=None):
    if h is None:
        h=[False]*ln
    if r is None:
        r=[]
    rc=r.copy()
    if sum(h)==ln:
        res.append(rc.copy())
        return
    for j in range(ln):
        
        if not h[j]:
            h[j]=True
            r.append(nums[j])
            dfs(i+1,r.copy(),h.copy())
        if r:
            r.pop()
        if i<ln:
            h[i]=False
dfs(0)
print(res)
