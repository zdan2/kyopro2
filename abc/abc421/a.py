n=int(input())
a=[input() for _ in range(n)]
x,y=input().split()
print('Yes' if a[int(x)-1]==y else 'No')