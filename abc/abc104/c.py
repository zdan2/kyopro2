d,g=map(int,input().split())
s=[[(i+1)*100]+list(map(int,input().split())) for i in range(d)]
a=float('inf')
for i in range(2**d):
    c=0
    solve=0
    ss=s.copy()
    for j in range(d):
        if (i>>j) & 1:
           c+=s[j][2]
           c+=s[j][0]*s[j][1]
           solve+=s[j][1]
           ss[j]=[0,0,0]
    if c>=g:
        a=min(a,solve)
        continue
    for point,nums,bonus in ss[::-1]:
        if point==0:
            continue
        if c+nums*point+bonus>=g:
            for i in range(nums):
                c+=point
                solve+=1
                if c>=g:
                    a=min(a,solve)
                    break
            else:
                a=min(a,solve)
        else:
            c+=point*nums+bonus
            solve+=nums
print(a)