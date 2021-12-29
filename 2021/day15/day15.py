from collections import defaultdict

def main():
    grid = load_data()
    print("Part One:", part_one(grid))
    print("Part Two:", part_two(grid))

def load_data():
    with open('input') as data:
        return [list(map(int, r.strip())) for r in data.readlines()]

def build_graph(grid):
    graph = defaultdict(dict)
    height, width = len(grid), len(grid[0])
    for i1, r in enumerate(grid):
        for i2, _ in enumerate(r):
            if 0 < i1:
                graph[(i1, i2)][(i1-1, i2)] = int(grid[i1-1][i2])
            if i1 < height-1:
                graph[(i1, i2)][(i1+1, i2)] = int(grid[i1+1][i2])
            if 0 < i2:
                graph[(i1, i2)][(i1, i2-1)] = int(r[i2-1])
            if i2 < width-1:
                graph[(i1, i2)][(i1, i2+1)] = int(r[i2+1])
    graph[(height-1,width-1)]
    return graph

def dijkstra(graph, start, end):
    dist = {v:float("inf") for v in graph.keys()}
    dist[start] = 0
    queue = [(0, start)]
    while queue:
        alt, v1 = min(queue)
        queue.remove((alt, v1))
        if v1[1] == end:
            return alt, dist
        elif v1 == end:
            return alt
        for v2 in graph[v1]:
            alt = dist[v1] + graph[v1][v2]
            if alt < dist[v2]:
                dist[v2] = alt
                queue.append((alt, v2))
    return None

def part_one(grid):
    return dijkstra(build_graph(grid), (0, 0), (len(grid)-1, len(grid[0])-1))

def part_two(grid):
    height, width = len(grid), len(grid[0])
    def expand_grid():
        new_grid = [[0 for _ in range(width*5)] for _ in range(height*5)]
        for dx in range(5):
            for dy in range(5):
                for iy,row in enumerate(grid):
                    for ix,n in enumerate(row):
                        new_val = n+dx+dy if n+dx+dy < 10 else n+dx+dy-9
                        new_grid[iy+dy*height][ix+dx*width] = new_val
        return new_grid
    return dijkstra(build_graph(expand_grid()), (0, 0), (height*5-1, width*5-1))

if __name__ == "__main__":
    main()
