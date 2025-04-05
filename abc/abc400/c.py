n=int(input())
r=[]
a=set()
i=1
while int((n/(2**i))**0.5)>0:
    r.append(int((n/(2**i))**0.5))
    i+=1
for i,j in enumerate(r):
    for k in range(1,j+1):
        a.add(2**(i+1)*k*k)
print(len(a))