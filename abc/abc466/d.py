n,m=map(int,input().split())
sy=set()
sx=set()
a=0
q=[list(map(int,input().split())) for _ in range(m)][::-1]
for y,x in q:
    if y in sy or x in sx:
        sy.add(y)
        sx.add(x)
        continue
    a+=1
    sy.add(y)
    sx.add(x)
print(a)