a,r,n=map(int,input().split())
if r==1:
    print(a)
    exit()
for i in range(1,n):
 if a*r**i>10**9:
    print('large')
    break
else:
    print(a*r**(n-1))
