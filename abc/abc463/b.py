n,x=input().split()
n=int(n)
x=ord(x)-ord('A')
for _ in range(n):
    if input()[x]=='o':
        print('Yes')
        exit()
print('No')