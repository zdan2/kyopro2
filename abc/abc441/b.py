n,m=map(int,input().split())
t=set(input())
a=set(input())
b=t&a
k=int(input())
for _ in range(k):
    c=set(input())
    r='Unknown'
    if len(c)==len(c&t):
        r='Takahashi'
    if len(c)==len(c&a):
        r='Aoki'
    if len(c)==len(c&b):
        r='Unknown'
    print(r)