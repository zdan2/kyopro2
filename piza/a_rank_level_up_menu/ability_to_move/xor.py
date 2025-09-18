n=int(input())
a=list(map(int,input().split()))
x=a[0]
for e in a[1:]:
    x^=e
print(x)