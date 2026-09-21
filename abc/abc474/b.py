n=int(input())
a=list(map(int,input().split()))
for i in range(n//10):
    for e in a[i*10:i*10+10]:
        if e>i*10+10:
            print('No')
            exit()
print('Yes')