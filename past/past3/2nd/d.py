from collections import defaultdict
d=defaultdict(list)
num=[
    '.###..#..###.###.#.#.###.###.###.###.###.',
    '.#.#.##....#...#.#.#.#...#.....#.#.#.#.#.',
    '.#.#..#..###.###.###.###.###...#.###.###.',
    '.#.#..#..#.....#...#...#.#.#...#.#.#...#.',
    '.###.###.###.###...#.###.###...#.###.###.'
]
for i in range(10):
    for j in range(5):
        d[i].append(num[j][4*i:4*i+4])
n=int(input())
mx=[input() for _ in range(5)]
r=''
for i in range(n):
    s=[]
    for j in range(5):
        s.append(mx[j][4*i:4*i+4])
    for k,v in d.items():
        if s==v:
            r+=str(k)
print(r)