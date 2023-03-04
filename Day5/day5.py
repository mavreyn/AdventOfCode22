# Part 1 Find which crates end on top

import re
from collections import deque

def crates_top():
    NSTACKS = 9
    STT_HT = 8

    stacks = [deque() for _ in range(NSTACKS)]

    with open('re.txt') as f:
        # Read the diagram
        for _ in range(STT_HT):
            ln = f.readline()

            for i in range(NSTACKS):
                if ln[4*i+1] != ' ':
                    stacks[i].appendleft(ln[4*i+1])

        [print(s) for s in stacks]

        # Skip to instructions
        f.readline()
        f.readline()

        for ln in f.readlines():
            # Nice solution to parse data
            parse = re.findall('\d+', ln.strip('\n'))
            am, fr, to = [int(p) for p in parse]
            print(am, fr, to)

            # Pop and append
            for _ in range(am):
                curr_crate = stacks[fr-1].pop()
                stacks[to-1].append(curr_crate)

        [print(s) for s in stacks]
        [print(s[len(s)-1], end='') for s in stacks]
            
# Part 2 CrateMover 9001 moves multiple boxes
# Very similar
def crates_top_mult_move():
    NSTACKS = 9
    STT_HT = 8


    stacks = [deque() for _ in range(NSTACKS)]

    with open('re.txt') as f:
        # Read the diagram
        for _ in range(STT_HT):
            ln = f.readline()

            for i in range(NSTACKS):
                if ln[4*i+1] != ' ':
                    stacks[i].appendleft(ln[4*i+1])

        [print(s) for s in stacks]

        # Skip to instructions
        f.readline()
        f.readline()

        for ln in f.readlines():
            # Nice solution to parse data
            parse = re.findall('\d+', ln.strip('\n'))
            am, fr, to = [int(p) for p in parse]
            print(am, fr, to)

            # Gather crates
            crates = [stacks[fr-1].pop() for _ in range(am)]
            stacks[to-1].extend(reversed(crates))

        [print(s) for s in stacks]
        [print(s[len(s)-1], end='') for s in stacks]

crates_top_mult_move()