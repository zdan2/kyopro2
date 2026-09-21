n=int(input())
a=list(map(int,input().split()))
s=a[:3]
s.sort(reverse=True)
for i in range(3,n):
    print(s[-1])
    if a[i]>s[-1]:
        s.pop()
        s.append(a[i])
        s.sort(reverse=True)
print(s[-1])