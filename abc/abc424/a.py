a,b,c=map(int,input().split())
if a==b and a+b>c or a==c and a+c>b or b==c and b+c>a:
    print('Yes')
else:
    print('No')