n=int(input())
t=list(map(int,input().split()))
def dfs(arr,i=1):
    if i>n:
        return
    print(arr[i-1])
    dfs(arr,i*2)
    dfs(arr,i*2+1)
dfs(t)