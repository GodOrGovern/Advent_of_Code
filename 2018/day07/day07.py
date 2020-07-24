''' https://adventofcode.com/2018/day/7 '''

class Node:
    ''' Node data structure to represent each step, including the time left to complete it and what steps it depends on '''
    def __init__(self, name=None):
        self.name = name
        self.time = None if name is None else name + 61
        self.parents = [None for x in range(26)]
    def __repr__(self):
        return chr(self.name + 65)
    def add_parent(self, parent):
        self.parents[parent.name] = parent
    def dec_time(self, time):
        self.time -= time

def main():
    ''' Driver function '''
    input_file = '/home/david/Documents/Programs/Advent_Code/day07/input'
    nodes = [build_tree(input_file), build_tree(input_file)]
    order = get_order(nodes[0])
    order = ''.join([chr(node.name + 65) for node in order])
    print(f'Part One: {order}')
    print(f'Part Two: {get_time(nodes[1])}')

def build_tree(file_name):
    ''' Build tree of 'nodes' from restrictions given in 'file_name' '''
    nodes = [Node() for x in range(26)]
    with open(file_name) as data:
        for line in data:
            child = check_nodes(ord(line[36]) - 65, nodes)
            parent = check_nodes(ord(line[5]) - 65, nodes)
            child.add_parent(parent)
    return nodes

def check_nodes(name, nodes):
    ''' Check if the node with a given 'name' already exists. If it does,
    return it. If it doesn't, create it and then return it '''
    if nodes[name].name == name:
        return nodes[name]
    nodes[name] = Node(name)
    return nodes[name]

def get_order(nodes):
    ''' Return the order in which the instructions are completed '''
    order = []
    orphan = find_orphan(nodes)
    while orphan != None:
        order.append(orphan)
        del_orphan(nodes, orphan)
        orphan = find_orphan(nodes)
    return order

def get_time(nodes):
    ''' Return how long it takes to complete all of the instructions '''
    time = 0
    order = []
    orphans = load_orphans([], nodes)
    while len(orphans) != 0:
        min_orphan = min(orphans, key=lambda x: x.time)
        time += min_orphan.time
        orphans.remove(min_orphan)
        [orphan.dec_time(min_orphan.time) for orphan in orphans]
        order.append(min_orphan)
        del_orphan(nodes, min_orphan)
        orphans = load_orphans(orphans, nodes)
    return time

def load_orphans(orphans, nodes):
    ''' Load the first five orphans found by 'find_orphan()'. If
    'find_orphan()' returns None, return the orphans found so far '''
    orphan = find_orphan(list(set(nodes) - set(orphans)))
    while orphan != None and len(orphans) != 5:
        orphans.append(orphan)
        orphan = find_orphan(list(set(nodes) - set(orphans)))
    return orphans

def find_orphan(nodes):
    ''' Find an 'orphan'. If multiple exist, return the one with the lowest
    'name'. If none exist, return None '''
    orphans = []
    for node in nodes:
        if node.parents.count(None) == len(node.parents):
            orphans.append(node)
    if len(orphans) > 0:
        return min(orphans, key=lambda x: x.name)
    return None

def del_orphan(nodes, orphan):
    ''' Remove 'orphan' from the parents attribute of all nodes in 'nodes' '''
    for node in nodes:
        node.parents[orphan.name] = None
    nodes.remove(orphan)

if __name__ == "__main__":
    main()