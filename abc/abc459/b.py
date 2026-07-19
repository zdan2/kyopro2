input()
a=[(ord(e[0])-ord('a')) for e in input().split()]
a=[e//3+2 if e<15 else 7 if 14<e<19 else 8 if 18<e<22 else 9 for e in a]
print(''.join(map(str,a)))