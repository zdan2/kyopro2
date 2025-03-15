def f(n):
    sqrn=int(n**0.5)+1
    r=set()
    for i in range(1,sqrn):
        if n%i==0:
            r.add(i)
            r.add(n//i)
    return len(r)

x,y=map(int,input().split())

fx=f(x)
fy=f(y)

if fx>fy:
    print('X')
elif fy>fx:
    print('Y')
else:
    print('Z')