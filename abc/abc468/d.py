s=list(input())
n=len(s)
c=0
for i in range(n):
    l,r=i,i
    d=0
    while l>=0 and r<n:
        if s[l]!=s[r]:
            d+=1
        if d>1:
            break
        c+=1
        l-=1
        r+=1
    l,r=i,i+1
    d=0
    while l>=0 and r<n:
        if s[l]!=s[r]:
            d+=1
        if d>1:
            break
        c+=1
        l-=1
        r+=1
print(c)