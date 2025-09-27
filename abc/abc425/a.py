n=int(input())
r=0
p=-1
for i in range(1,n+1):
    r+=p**(i%2)*(i**3)
print(r)