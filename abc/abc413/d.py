from fractions import Fraction
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    a=sorted(a,key=lambda x:abs(x))
    r=Fraction(a[1],a[0])
    for i in range(1,n):
        if Fraction(a[i],a[i-1])!=r:
            print('No')
            break
    else:
        print('Yes')