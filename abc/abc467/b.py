n=int(input())
r=0
for _ in range(n):
    a,b,c=input().split()
    if c=='keep':
        r+=int(b)-int(a)
print(r)