s=input()
so_far={'A':0,'B':0}
r=0
for i in range(len(s)):
    if s[i]=='A':
        so_far['A']+=1
    elif s[i]=='B':
        if so_far['A']>0:
            so_far["B"]+=1
            so_far['A']-=1
    else:
        if so_far['B']>0:
            r+=1
            so_far['B']-=1
print(r)