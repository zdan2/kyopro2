n=int(input())
b=[list(map(int,input().split())) for _ in range(n+1)]
mb=b[0]
b.sort()
print(b.index(mb)+1)
b4=[[m+(12 if m<4 else 0),d] for m,d in b]
b4.sort()
while True:
    if b4[0]==[4,1]:
        del b4[0]
        b4.append([4,1])
    else:
        break
if mb[0]<4:
    mb=[mb[0]+12,mb[1]]
print(b4.index(mb)+1)