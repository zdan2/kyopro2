n,m=map(int,input().split())
a=list(map(int,input().split()))
def f(arr,k,c=None):
    if c==None:
        c=0
    if len(arr)==0:
        return True
    c+=arr[0]
    if c>k:
        return False
    return f(arr[1:],k,c)

print('Yes' if f(a,m) else 'No')