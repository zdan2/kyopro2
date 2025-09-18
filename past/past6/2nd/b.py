s=input()
s=s.replace('past','*').replace('post','o')
print(s.index('o')+1 if 'o' in s else 'none')