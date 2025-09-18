def gen_palindromes(limit):
    max_len = len(str(limit))
    for length in range(1, max_len + 1):
        half_len = (length + 1) // 2
        start = 0 if length == 1 else 10 ** (half_len - 1)
        end   = 10 ** half_len
        odd   = length & 1
        for half in range(start, end):
            pal = half
            rev = half // 10 if odd else half
            while rev:
                pal = pal * 10 + rev % 10
                rev //= 10
            if pal > limit:
                return
            yield pal

def is_base_pal(x, base):
    if x == 1:
        return True
    digits = []
    while x:
        digits.append(x % base)
        x //= base
    return digits == digits[::-1]


b = int(input())
n = int(input())
total = 0
for p in gen_palindromes(n):
    if is_base_pal(p, b):
        total += p
print(total)

