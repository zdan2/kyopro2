from functools import lru_cache

@lru_cache
def ld(s,t):
    if not s:
        return len(t)
    if not t:
        return len(s)
    if s[0]==t[0]:
        return ld(s[1:],t[1:])
    l1=ld(s[1:],t)
    l2=ld(s,t[1:])
    l3=ld(s[1:],t[1:])
    return 1+min(l1,l2,l3)

n,m=map(int,input().split())
s=input()
t=input()
print(ld(s,t))