h,w=map(int,input().split())
s=[list(input()) for _ in range(h)]
t=[list(input()) for _ in range(h)]
for i in range(4):
    for j in range(len(t)):
        if set(t[j])!={'.'}:
            break
    t=t[j:]
    t=list(zip(*t[::-1]))
rt=[t]
for _ in range(3):
    t=list(zip(*t[::-1]))
    rt.append(t)
for stamp in rt:
    sh=len(stamp)
    sw=len(stamp[0])
    for i in range(h-sh+1):
        for j in range(w-sw+1):
            f=1
            for k in range(sh):
                for l in range(sw):
                    if stamp[k][l]=='#' and s[i+k][j+l]=='#':
                        f=0
                        break
                if f==0:
                    break
            if f:
                print('Yes')
                exit()
print('No')