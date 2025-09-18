t=input()
u=input()
lt=len(t)
lu=len(u)
h=0
for i in range(lt-lu+1):
    for j in range(lu):
        if t[i+j]=='?':
            continue
        if t[i+j]!=u[j]:
            break
    else:
        h=1
        break
if h:
    print('Yes')
else:
    print('No')
    