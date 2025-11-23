n=int(input())
a=[(*map(int,input().split()),i+1) for i in range(n)]
b=sorted([(a+b,a,b,i) for a,b,i in a], key=lambda x:[x[0],x[2],x[3]])
print(*[x[-1] for x in b][::-1])