def g(n):
    s_n = str(n)
    max_len = len(s_n)

    for length in range(1, max_len + 1):
        half_len = (length + 1) // 2
        start = 0 if length == 1 else 10 ** (half_len - 1)
        end   = 10 ** half_len

        for half in range(start, end):
            half_str = str(half)
            if length % 2:
                pal = int(half_str + half_str[-2::-1]) 
            else:
                pal = int(half_str + half_str[::-1]) 
            if pal > n:
                if length == max_len:
                    return
                break
            yield pal
b=int(input())
n=int(input())
r=list(g(n))
def f(n,b):
    if n==0:
        return ''
    return f(n//b,b)+str(n%b)
a=0
for e in r:
    s=f(e,b)
    if s==s[::-1]:
        a+=e
print(a)    