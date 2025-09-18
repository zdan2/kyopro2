s=list(input())
s=[int(i) for i in s]
ls=len(s)
r=0
b=0
while s:
    c=s.pop()
    d=(c-b)%10
    r+=d
    b=(b+d)%10
print(r+ls) 