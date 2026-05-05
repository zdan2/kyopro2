n=int(input())
a=list(map(int,input().split()))
l=0
add=0
xor=0
c=0
cr=0
for r in range(n):
    add+=a[r]
    xor^=a[r]
    if add==xor:
        continue
    c+=(r-l)*(r-l+1)//2
    c-=(cr-l)*(cr-l+1)//2
    cr=r
    while add!=xor and l<r:
        add-=a[l]
        xor^=a[l]
        l+=1
c+=(n-l)*(n-l+1)//2
c-=(cr-l)*(cr-l+1)//2      
print(c)