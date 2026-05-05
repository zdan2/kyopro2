h,w=map(int,input().split())
r=[['#']*w for _ in range(h)]
for i in range(1,h-1):
    for j in range(1,w-1):
        r[i][j]='.'
for l in r:
    print(''.join(l))