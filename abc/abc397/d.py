import math
n=int(input())
md=int((4*n)**(1/3))+1
for d in range(1,md+1):
    if d**3>4*n:
        break
    h=3*d*(4*n-d**3)
    t=math.isqrt(h)
    if t*t!=h:
        continue
    m=t-3*d*d
    if m<0:
        continue
    if m%(6*d)!=0:
        continue
    y=m//(6*d)
    if y<=0:
        continue
    x=y+d
    print(int(x),int(y))
    exit()
print(-1)