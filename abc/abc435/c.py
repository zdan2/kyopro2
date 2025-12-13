n=int(input())
a=list(map(int,input().split()))
h=a[0]
for i in range(1,n):
    h-=1
    if h==0:
        print(i)
        exit()
    h=max(h,a[i])
print(n)