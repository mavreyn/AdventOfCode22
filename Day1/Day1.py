# Day 1 Part 1
def Highest():
    with open('day1InputRe.txt') as f:
        curr = 0
        max_ = 0

        for line in f:
            if line.strip():
                curr += int(line)
            else:
                max_ = curr if curr > max_ else max_
                curr = 0

    print(max_)

# Day 1 Part 2
def TopThree():
    with open('day1InputRe.txt') as f:
        curr = 0
        sums = []
        total3 = 0

        for line in f:
            if line.strip():
                curr += int(line)
            else:
                sums.append(curr)
                curr = 0

        sums.sort(reverse=True)
        print(sums[:3])

        for i in range(3):
            total3 += sums[i]
        print(total3)

TopThree()
