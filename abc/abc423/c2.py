n,r=map(int,input().split())
l=list(input())
c=1 if l[r-1]=='0' else 2
j=1
for i in range(r-1):
    if j and l[i]=='1':
       continue
    if l[i]=='0':
       j=0
    if l[i]=='0':
        c+=1
    else:
        c+=2
j=1
for i in range(n-1,r,-1):
    if j and l[i]=='1':
       continue
    if l[i]=='0':
       j=0
    if l[i]=='0':
        c+=1
    else:
        c+=2
print(c) 