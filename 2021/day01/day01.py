def main():
    data = load_data('input')
    print("Part one:", larger_than_prev(data))
    print("Part two:", larger_than_prev_window(data))

def load_data(f):
    ''' Return the list of integers stored in the file 'input' '''
    with open('input') as data:
        return list(map(int,  data))

def larger_than_prev(data):
    ''' Return the number of elements that are greater than the previous
    element in the list 'data' '''
    return sum(data[i-1] < data[i] for i in range(1, len(data)))

def larger_than_prev_window(data):
    ''' A three-measurement sliding window sum starting at some index 'i' is
    equal to sum(data[i:i+3]). Return the number of three-measurement sliding
    window sums starting at 'i' that are less than the sum starting at 'i+1'
    for all 'i' in the range 0 <= i < len(data)-2  '''
    count = 0
    cur_sum = sum(data[:3])
    for i in range(1, len(data)-2):
        next_sum = cur_sum + data[i+2] - data[i-1]
        count += cur_sum < next_sum
        cur_sum = next_sum
    return count

if __name__ == "__main__":
    main()
