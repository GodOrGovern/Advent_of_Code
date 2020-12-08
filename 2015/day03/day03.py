orig = (0, 0)
santa = [(0, 0), (0, 0)]
visited = [{(0, 0)}, {(0, 0)}]
delta = {'^': (0, 1), 'v': (0, -1), '<': (-1, 0), '>': (1, 0)}
for i, d in enumerate(open('input').read().strip()):
    orig = (orig[0] + delta[d][0], orig[1] + delta[d][1])
    santa[i%2] = (santa[i%2][0] + delta[d][0], santa[i%2][1] + delta[d][1])
    visited[0].add(orig)
    visited[1].add(santa[i%2])
print(len(visited[0]), len(visited[1]))
