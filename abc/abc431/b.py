x=int(input())
n=int(input())
w=list(map(int,input().split()))
t=[1]*n
q=int(input())
for _ in range(q):
    p=int(input())-1
    x+=t[p]*w[p]
    print(x)
    t[p]*=-1