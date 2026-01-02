n=int(input())
d={}
word=[input() for _ in range(n)]
for i in range(n):
    cd=d
    for e in word[i]:
        if e not in cd:
            cd[e]={'co':0}
        cd=cd[e]
        cd['co']+=1
    cd['*']=None
for e in word:
    cd=d
    r=len(e)
    for i,l in enumerate(e):
        cd=cd[l]
        if cd['co']==1:
            r=i
            break
    print(r)