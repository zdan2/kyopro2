def f(h):
    if h<=1:
        return 1
    return 1+f(h//2)*2
n=int(input())
print(f(n))