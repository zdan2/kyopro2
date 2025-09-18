def f(n):
    sqrt=int(n**0.5)+1
    s=set()
    for i in range(1,sqrt+1):
        if n%i==0:
            s.add(i)
            s.add(n//i)
    return len(s)
x,y=map(int,input().split())
if f(x)>f(y):
    print('X')
elif f(y)>f(x):
    print('Y')
else:
    print('Z')