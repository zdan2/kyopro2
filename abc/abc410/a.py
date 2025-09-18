input()
a=list(map(int,input().split()))
k=int(input())
print(sum(k<=e for e in a))