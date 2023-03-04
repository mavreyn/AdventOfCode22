# Part 1 finding sum of Priorities
def priority(s: str):
    return ord(s) - 64 + 26 if s.isupper() else ord(s) - 96

def pri_tot():
    total = 0

    with open('re.txt') as f:
        # Split into rucksacks
        for line in f:
            line = line.strip('\n')
            mid = len(line)//2
            r1, r2 = line[:mid], line[mid:]
            print(r1, r2)

            # Find intersections
            comm = list(set(r1) & set(r2))[0]
            print(comm)
            print(priority(comm))

            total += priority(comm)

    print(total)


def badge_find():
    total = 0

    with open('re.txt') as f:
        lines = [l.strip('\n') for l in f.readlines()]

        # Split into groups of 3
        for i in range(0, len(lines), 3):
            comm = list(set(lines[i]) & set(lines[i+1]) & set(lines[i+2]))[0]
            print(comm)

            # Add priority to total
            total += priority(comm)
    
    print(total)


badge_find()