s=-1
c=0
n=int(input())
for i in range(n):
    q=input()
    if q=='login':
        s=1
    if q=='logout':
        s=-1
    if q=='private' and s==-1:
        c+=1
print(c)