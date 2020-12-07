def main():
    paper, ribbon = 0, 0
    for line in open('input'):
        l, w, h = map(int, line.strip().split('x'))
        sides = [l*w, l*h, h*w]
        paper += 2*sum(sides) + min(sides)
        ribbon += 2*min([l+w,l+h,w+h]) + l*w*h
    print(paper, ribbon)

if __name__ == "__main__":
    main()
