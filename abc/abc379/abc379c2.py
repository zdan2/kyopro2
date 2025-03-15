n, m = map(int, input().split())
x = list(map(int, input().split()))
a = list(map(int, input().split()))
if sum(a) != n:
    print(-1)
    exit()

c = 0
fixed_positions = set()
remaining_n = n

for i in range(m - 1, -1, -1):
    xe = x[i]
    ae = a[i]
    
    if ae == 1:
        fixed_positions.add(xe)
    else:
        movable_positions = remaining_n - len(fixed_positions)
        
        fixed_before_xe = len([pos for pos in fixed_positions if pos < xe])
        
        adjusted_xe = xe - fixed_before_xe
        adjusted_ae = ae
        
        c += (movable_positions - adjusted_xe - adjusted_ae + 1 + movable_positions - adjusted_xe) * adjusted_ae // 2
        
        remaining_n -= ae

        if remaining_n < adjusted_xe - 1:
            print(-1)
            exit()

print(c)
