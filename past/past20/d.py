d={'v':'<','<':'^','^':'>','>':'v'}
n=int(input())
mx=[list(input()) for _ in range(n)]
tx=[list(r)[::-1] for r in zip(*mx)]
for i in range(n):
    for j in range(n):
        tx[i][j]=d[tx[i][j]]
for r in tx:
    print(''.join(r))