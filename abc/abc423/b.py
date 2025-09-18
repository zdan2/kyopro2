input()
print(max(0,len(input().replace(' ','').lstrip('0').rstrip('0'))-1))