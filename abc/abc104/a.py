n=int(input())
a=0 if n<1200 else 1 if n<2800 else 2
print(['ABC','ARC','AGC'][a])