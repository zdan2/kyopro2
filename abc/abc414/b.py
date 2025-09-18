n=int(input())
r=0
s=''
for _ in range(n):
    c,l=input().split()
    l=int(l)
    r+=l
    if r>100:
        print('Too Long')
        break
    s+=c*l
else:
    print(s)