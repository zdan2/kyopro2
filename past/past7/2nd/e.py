n=int(input())
r=-1
for i in range(30):
    if n%3!=0 and r==-1:
        if (n-1)%3==0:
            r=30-i
            n-=1
        else:
            print(-1)
            exit()
    elif n%3!=0 and r!=-1:
        print(-1)
        exit()
    n//=3
if n:
    print(r)
else:
    print(-1)