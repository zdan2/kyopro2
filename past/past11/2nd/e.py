#m=int(input())
m=100
r=[]
rb=[]
for n in range(m):
    a=int(-1/2+(1+4*n)**0.5/2)
    b=a*a+a
    c=n-b
    if c>a+1:
        c-=b-a
    r.append(c)
    rb.append(a)
    
print(r)
print(rb)