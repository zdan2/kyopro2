def f(s,l,r):
    if s[l-1]!='o':
        return False
    if l==r:
        return True
    return f(s,l+1,r)

n,l,r=map(int,input().split())
s=input()
print('Yes' if f(s,l,r) else 'No')