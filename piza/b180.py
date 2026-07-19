m=[list(input()) for _ in range(7)]
while True:
    if m[0][0]=='.':
        break
    m=[list(r)[::-1] for r in zip(*m)]
c=0
for i in range(1,6):
    for j in range(1,6):
        if m[i][j]=='#':
            c+=2**(5*(i-1)+(j-1))
print(c)