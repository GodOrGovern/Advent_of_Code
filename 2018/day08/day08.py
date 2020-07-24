''' https://adventofcode.com/2018/day/8 '''

class Node:
    ''' Implements a node data structure based off the description given '''
    def __init__(self, child_num, meta):
        self.child = []
        self.child_num = child_num
        self.meta = []
        self.metadata = meta
        self.parent = None
    def add_child(self, child):
        self.child.append(child)
        child.parent = self
    def add_meta(self, meta):
        self.meta.append(meta)

def main():
    ''' Driver function '''
    input_file = '/home/david/Documents/Programs/Advent_Code/day08/input'
    nums = load_data(input_file)
    checksum, root = load_nodes(nums)
    print(f'Part One: {checksum}')
    value = node_value(root)
    print(f'Part Two: {value}')

def load_data(file_name):
    ''' Return list of numbers from 'file_name' '''
    nums = []
    with open(file_name) as data:
        for line in data:
            nums = [int(x) for x in line.split()]
    return nums

def load_nodes(nums):
    ''' Load all nodes and compute the sum of all metadata entries. Return the
    sum and the root node '''
    checksum = 0
    root = Node(nums.pop(0), nums.pop(0))
    cur_node = root
    while cur_node:
        if cur_node.child_num != len(cur_node.child):
            next_node = Node(nums.pop(0), nums.pop(0))
            cur_node.add_child(next_node)
            cur_node = next_node
        else:
            while cur_node.metadata != len(cur_node.meta):
                cur_node.add_meta(nums.pop(0))
            checksum += sum(cur_node.meta)
            cur_node = cur_node.parent
    return checksum, root

def node_value(cur_node):
    ''' Return the value of 'cur_node' '''
    if not cur_node.child_num:
        return sum(cur_node.meta)
    value = 0
    for i in cur_node.meta:
        if 1 <= i <= cur_node.child_num:
            value += node_value(cur_node.child[i-1])
    return value

if __name__ == "__main__":
    main()