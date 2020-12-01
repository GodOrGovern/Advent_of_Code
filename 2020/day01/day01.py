def main():
    nums = []
    with open('input') as data:
        for num in data:
            nums += [int(num)]
    for i, x in enumerate(nums[:-1]):
        for y in nums[i+1:]:
            if x + y == 2020:
                print(x*y)
    for i1, x in enumerate(nums[:-2]):
        for i2, y in enumerate(nums[i1+1:-1]):
            for z in nums[i2+1:]:
                if x + y + z == 2020:
                    print(x*y*z)

if __name__ == "__main__":
    main()
