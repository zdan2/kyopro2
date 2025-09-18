n,m=map(int,input().split())
c=0
for i in range(m+1):
    c+=n**i
    if c>10**9:
        print('inf')
        exit()
print(c)