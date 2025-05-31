n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=0
if a==b:
    print('Yes')
    exit()
h=False
for i in range(n-1):
    if a[i]!=b[i]:
        if a[i+1]==b[i] and a[i]==b[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
            c+=1
        elif i+2<n:
            if a[i+2]==b[i]:
                a[i],a[i+1],a[i+2]=a[i+2],a[i],a[i+1]
                c+=2
            elif a[i]==b[i+2]:
                a[i],a[i+1],a[i+2]=a[i+1],a[i+2],a[i]
                c+=2
    if a[i]==a[i+1]:
        h=True
    if i>1 and a[i-1]==a[i]:
        h=True
if a==b and c==2:
    print('Yes')
elif a==b and c==1 and h:
    print('Yes')
else:
    print('No')