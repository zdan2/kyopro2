h,w,n=map(int,input().split())
mx=[set(map(int,input().split())) for _ in range(h)]
s=set(int(input()) for _ in range(n))
print(max(len(a&s) for a in mx))