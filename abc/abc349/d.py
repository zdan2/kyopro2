l,r=map(int,input().split())
a=[]
while l<r:
    i=0
    while l%pow(2,i+1)==0 and l+pow(2,i+1)<=r:
        i+=1
    a.append((l,l+pow(2,i)))
    l+=pow(2,i)
print(len(a))
for e in a:
    print(*e)