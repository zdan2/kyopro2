n,m=map(int,input().split())
for i in range(n):
    if i<m:
        e='OK'
    else:
        e='Too Many Requests'
    print(e)