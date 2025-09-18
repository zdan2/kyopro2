s=set(chr(i) for i in range(ord('a'),ord('a')+26))
t=set(input())
print(list(t^s).pop())