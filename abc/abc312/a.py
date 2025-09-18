d=set()
for i in range(7):
    t=''
    for k in range(3):
        t+=chr(ord('A')+(i+k*2)%7)
    d.add(t)
print('Yes' if input() in d else 'No')