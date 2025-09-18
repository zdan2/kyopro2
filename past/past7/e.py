n=int(input())
    
if n%3!=0 or n<3**30:
    print(-1)
    exit()
c=0
for i in range(30):
    if n%3==0:
        n//=3
    else:
        break
    
if (n-1)%3==0:
    print(30-i)
else:
    print(-1)