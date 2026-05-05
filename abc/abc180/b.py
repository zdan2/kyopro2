n=int(input())
a=[abs(e) for e in map(int,input().split())]
print(sum(a))
print(sum(x*x for x in a)**0.5)
print(max(a))