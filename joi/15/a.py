a=[int(input()) for _ in range(6)]
a1=sorted(a[:4])
a2=sorted(a[4:])
print(sum(a1[1:])+a2[-1])