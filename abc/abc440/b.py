input()
a=list(map(int,input().split()))
print(*[i for i,_ in sorted([(i+1,e) for i,e in enumerate(a)],key=lambda x:x[1])][:3])