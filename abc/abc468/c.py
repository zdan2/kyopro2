from math import factorial
def f(arr):
    l=len(arr)
    r=0
    s=set(range(1,l+1))
    for i in range(l):
        a=sum(e<arr[i] for e in s)
        r+=a*factorial(l-i-1)
        s.remove(arr[i])
    return r+1
input()
a=list(map(int,input().split()))
b=list(map(int,input().split()))
print(max(0,f(b)-f(a)-1))