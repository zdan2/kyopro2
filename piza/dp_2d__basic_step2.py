a=sorted(input())
if a[0]=='0':
    for i,e in enumerate(a):
        if e!='0':
            a[0],a[i]=a[i],a[0]
            break
print(''.join(a))