n=int(input())
mx=[list(input()) for _ in range(5)]


def t(g):
    a=[]
    l=len(g[0])
    for j in range(1,l,4):
        num=[]
        for i in range(5):
            num.append(g[i][j:j+3])   
        a.append(num)
    return a


b=[
list('.###..#..###.###.#.#.###.###.###.###.###.'),
list('.#.#.##....#...#.#.#.#...#.....#.#.#.#.#.'),
list('.#.#..#..###.###.###.###.###...#.###.###.'),
list('.#.#..#..#.....#...#...#.#.#...#.#.#...#.'),
list('.###.###.###.###...#.###.###...#.###.###.')
]

ref=t(b)

test=t(mx)
r=''
for i in range(n):
    for j in range(10):
        if test[i]==ref[j]:
            r+=str(j)
print(r)         