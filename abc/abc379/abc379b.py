n,k=map(int,input().split())
s=list(input())
r=[]
c=0
for i in range(n):
    if s[i]=='O':
        c+=1
    else:
        r.append(c)
        c=0
r.append(c)
print(sum(i//k for i in r))