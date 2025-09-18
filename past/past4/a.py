a=list(map(int,input().split()))
sa=sorted(a)
if sa[1]==a[0]:
    print('A')
elif sa[1]==a[1]:
    print('B')
else:
    print('C')