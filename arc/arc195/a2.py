n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
j=0
l=[]
for i in range(n):
    if b[j]==a[i]:
        l.append(i)
        if j==0:
            ns=i
        j+=1
    if j==m:
        ne=i
        break
else:
    print('No')
    exit()
j=m-1
r=[]
for i in range(n-1,-1,-1):
    if b[j]==a[i]:
        r.append(i)
        if j==m-1:
            me=i
        j-=1
    if j==-1:
        ms=i
        break
print('Yes' if r[::-1]!=l else 'No')