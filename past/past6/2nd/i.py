from collections import deque
h,w=map(int,input().split())
dp=[[0]*(h+w+1) for _ in range(h+w+1)]
q=deque()
mx=[list(map(int,input().split())) for _ in range(h)]
dp[0]=mx[0][0]
q.append((1,0,dp[0]))
q.append((0,1,dp[0]))
while q:
    y,x,p=q.popleft()
    for i in range(y+x,-1,-1):
        for j in range(y+x,-1,-1):
            
    
    

