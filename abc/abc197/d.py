import math
n = int(input())
theta = 2 * math.pi / n
x0, y0 = map(int, input().split())
x1, y1 = map(int, input().split())
cx = (x0 + x1) / 2
cy = (y0 + y1) / 2
vx = x1 - cx
vy = y1 - cy
r  = math.hypot(vx, vy)
ux = vx * math.cos(theta) - vy * math.sin(theta)
uy = vx * math.sin(theta) + vy * math.cos(theta)
p = (cx - ux, cy - uy)
print(*p) 
