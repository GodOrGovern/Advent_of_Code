face, pos = (0, 1), (0, 0)
twice = None
visited = set()
for move in open('input').read().strip().split(', '):
    face = [(-face[1], face[0]), (face[1], -face[0])][move[0] == 'R']
    for _ in range(int(move[1:])):
        pos = (pos[0] + face[0], pos[1] + face[1])
        twice = pos if pos in visited and twice == None else twice
        visited.add(pos)
print(sum(map(abs, pos)), sum(map(abs, twice)))
