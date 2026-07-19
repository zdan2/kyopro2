n=int(input())
a=0
l=1
r=2
while r<=n:
    print('?', l, r)
    if input() == 'Yes':
        a+=r-l
        r+=1
    else:
        l+=1
        if l==r:
            r+=1
print('!',a)