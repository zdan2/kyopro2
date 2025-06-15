t=int(input())
for _ in range(t):
    n=int(input())
    s=list(input())
    left=-1
    right=-1
    for i in range(n-1):
        if s[i]>s[i+1]:
            left=i
            break
    for i in range(left,n-1):
        if s[left]<s[i+1]:
            right=i
            break
    else:
        right=n-1
    a=s[left]
    del s[left]
    s.insert(right,a)
    print(''.join(s))