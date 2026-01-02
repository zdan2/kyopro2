n=int(input())-1
r=[]
for _ in range(3):
    r.append(chr(ord('a')+n%26))
    n//=26
print(''.join(r[::-1]))