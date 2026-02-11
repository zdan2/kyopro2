n=int(input())
a=sorted(list(map(int,input().split())))
if n%2==1:
    print(a[-1])
    exit()
l=[]
if n==2:
    if a[0]==a[1]:
        l.append(a[0])
    l.append(a[0]+a[1])
else:
    if a[0]==a[-1]:
        l.append(a[0])
    b=a.copy()
    while b and b[-1]==a[-1]:
        b.pop()
    m=len(b)
    if m>0 and m%2==0 and sum(b)//(m//2)==a[-1]:
        l.append(a[-1])
    if a[-1]+a[0]==a[-2]+a[1]:
        l.append(a[-1]+a[0])
print(*l)