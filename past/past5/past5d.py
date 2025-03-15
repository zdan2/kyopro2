n=int(input())
r=[]
for i in range(n):
    s=input()
    ls=len(s)
    for j in range(ls):
        if s[j]!='0':
            break
    ints=int(s[j:])
    r.append((ints,j))
sr=sorted(r,key=lambda x:[x[0],-x[1]])
for num,z in sr:
    print('0'*z+str(num))