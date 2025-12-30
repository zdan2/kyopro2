n, a, b, c, d = map(int, input().split())

diffs = set()
sums = set()
for _ in range(n):
    p, q = map(int, input().split())
    diffs.add(p - q)
    sums.add(p + q)

H = b - a + 1
W = d - c + 1

out_lines = []
for row in range(a, b + 1):
    line = ['.'] * W
    for col in range(c, d + 1):
        if (row - col) in diffs or (row + col) in sums:
            line[col - c] = '#'
    out_lines.append(''.join(line))

print('\n'.join(out_lines))