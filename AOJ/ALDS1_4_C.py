s=set()
n=int(input())
for _ in range(n):
    q,t=input().split()
    if q=='insert':
        s.add(t)
    else:
        if t in s:
            print('yes')
        else:
            print('no')