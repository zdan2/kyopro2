n=int(input())

def f(n):
    if n==0:
        return 0
    return f(n//10)+(n%10)**2
s=set()

while True:
    if n in s:
        print('No')
        exit()
    if n==1:
        print('Yes')
        exit()
    s.add(n)
    n=f(n)    