s=input()
print(''.join(a+b for a,b in zip(s,'o'*len(s)))[:-1])