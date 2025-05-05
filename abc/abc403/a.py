n=int(input())
a=list(map(int,input().split()))
print(sum(e for i,e in enumerate(a) if i%2==0))