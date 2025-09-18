n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=0
for i in range(n-1):
    if a[i]==b[i+1] and a[i+1]==b[i]:
        c+=1
if 1<=c<=2:
    print('Yes')
    exit()
c=0
for i in range(n-2):
    if (a[i]==b[i+1] and a[i+1]==b[i+2] and a[i+2]==b[i]) or (a[i]==b[i+2] and a[i+2]==b[i+1] and a[i+1]==b[i]):
        c+=1
if c==1:
    print('Yes')
    exit()
print('No')
