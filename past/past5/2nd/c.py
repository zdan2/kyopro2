n=int(input())
if n==0:
    print(0)
    exit()
i=1
r=''
a=[str(i) for i in range(10)]+[chr(i) for i in range(ord('A'),ord('A')+26)]
while n>0:
    c=n%36**i
    r+=a[c]
    n=n//36*i
print(r[::-1])