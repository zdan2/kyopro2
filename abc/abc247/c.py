def f(n):
    if n==1:
        return '1'
    return f(n-1)+' '+str(n)+' '+f(n-1)
n=int(input())
print(f(n))