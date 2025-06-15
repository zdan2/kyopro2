n=int(input())
a=list(map(int,input().split()))
while True:
    r=[]
    i=0
    s=min(a)
    f=0
    while i<len(a):
        if i+1<len(a) and (a[i]==s or a[i+1]==s) and abs(a[i]-a[i+1])<=1:
            r.append(a[i]+a[i+1])
            i+=2
            f=1
        else:
            r.append(a[i])
            i+=1
    if not f:
        break
    a=r
print('Yes' if len(r)==1 else 'No')