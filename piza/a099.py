def rotate(grid):
    return tuple(
        tuple(row[::-1])
        for row in zip(*grid)
    )


def reverse(grid):
    return tuple(
        tuple(reversed(row))
        for row in grid
    )


def normalize(grid):
    patterns = []
    current = grid
    for _ in range(4):
        patterns.append(current)
        current = rotate(current)
    current = reverse(grid)
    for _ in range(4):
        patterns.append(current)
        current = rotate(current)

    return min(patterns)

n = int(input())
shapes = set()
for _ in range(n):
    h, w = map(int, input().split())
    grid = tuple(tuple(input()) for _ in range(h))
    shapes.add(normalize(grid))
print(len(shapes))