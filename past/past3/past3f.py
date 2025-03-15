n=int(input())
r=[]
for _ in range(n):
   r.append(set(input()))

a=''
for i in range(n//2):
    for e in r[i]:
        if e in r[-(i+1)]:
            a+=e
            break
    else:
        print(-1)
        exit()
if n%2==1:
    a+=r[n//2].pop()

if n%2==0:
    print(a+a[::-1])
else:
    b=a[::-1]
    print(a+b[1:])
             