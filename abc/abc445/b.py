n=int(input())
a=[input() for _ in range(n)]
m=max([len(s) for s in a])
for s in a:
    b=(m-len(s))//2
    print('.'*b+s+'.'*b)