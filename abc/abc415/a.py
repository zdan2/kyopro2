def f(arr,target,i=0):
    if arr[i]==target:
        return True
    if i==len(arr)-1:
        return False
    return f(arr,target,i+1)
input()
a=list(map(int,input().split()))
x=int(input())
print('Yes' if f(a,x) else 'No')