input()
print('Yes' if any(a==b=='o' for a,b in zip(list(input()),list(input()))) else 'No')