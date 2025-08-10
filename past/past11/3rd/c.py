n,m=map(int,input().split())
a=10**9
b=n
s=''
for i in range(m):
    if b<=a:
        s+='o'
    else:
        break
    b*=n
print(s+'x'*(m-len(s)))        