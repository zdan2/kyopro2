n=int(input())
board=[list(input()) for _ in range(n)]

dyx=[(0,1),(1,0),(-1,0),(0,-1),(1,-1),(-1,1),(1,1),(-1,-1)]

def f(y,x,dy,dx):
    cy=y+dy
    cx=x+dx
    while 0<=cy<n and 0<=cx<n:
        if board[cy][cx]=='.':
            return False
        if board[cy][cx]=='B':
            return True
        cy+=dy
        cx+=dx
    return False
    
a=0
for i in range(n):
    for j in range(n):
        if board[i][j]=='.':
            for dy,dx in dyx:
                ny=i+dy
                nx=j+dx
                if 0<=ny<n and 0<=nx<n and board[ny][nx]=='W':
                    if f(ny,nx,dy,dx):
                        a+=1
                        break
print(a)