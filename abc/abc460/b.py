t=int(input())
for _ in range(t):
    a,b,c,d,e,f=map(int,input().split())
    g=(a-d)**2
    h=(b-e)**2
    i=(c+f)**2
    j=(c-f)**2
    if j<=g+h<=i:
        print('Yes')
    else:
        print('No')