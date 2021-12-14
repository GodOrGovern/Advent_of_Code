from collections import defaultdict

def main():
    data = load_data()
    print("Part One:", part_one(data))
    print("Part Two:", part_two(data))

def load_data():
    with open('input') as data:
        graph = defaultdict(set)
        for line in data:
            a,b = line.strip().split('-')
            graph[a].add(b)
            graph[b].add(a)
        return graph

def part_one(graph):
    def search(node, path, visited):
        if node in visited:
            return 0
        if node == 'end':
            return 1
        num_paths = 0
        for next_node in graph[node]:
            new_visited = visited|{node} if node.islower() else visited
            num_paths += search(next_node, path+(node,), new_visited)
        return num_paths
    return sum(search(node, ('start',), {'start'}) for node in graph['start'])

def part_two(graph):
    def search(node, path, visited, twice_small=False):
        if node in visited:
            if node == 'start' or twice_small:
                return 0
            twice_small = True
        if node == 'end':
            return 1
        num_paths = 0
        for next_node in graph[node]:
            new_visited = visited|{node} if node.islower() else visited
            num_paths += search(next_node, path+(node,), new_visited, twice_small)
        return num_paths
    return sum(search(node, ('start',), {'start'}) for node in graph['start'])

if __name__ == "__main__":
    main()

