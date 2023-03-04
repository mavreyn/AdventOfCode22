# Part 1 find sections that fully contain other sections

import re
import math

def sign(x: int):
    return abs(x)//x

def is_in(a1, a2):
    if a1[0] == a2[0] or a1[1] == a2[1]:
        return True
    else:
        return sign(int(a1[1])-int(a2[1])) == sign(int(a2[0])-int(a1[0]))

def full_contain():
    contains = 0

    with open('re.txt') as f:
        for l in f:
            # Use regex to split and | to define mult splitting chars
            nums = re.split('-|,', l.strip('\n'))
            print(nums)
           
            if is_in(nums[:2], nums[2:]):
                contains += 1
    
    print(contains)

# Part 2 find any overlapping sections
def set_sf(a, b):
    return set(range(a, b+1))

def overlap():
    overlaps = 0

    with open('re.txt') as f:
        for l in f:
            # Same regex again
            nums = [int(n) for n in re.split('-|,', l.strip('\n'))]
            s1, s2 = set_sf(nums[0], nums[1]), set_sf(nums[2], nums[3])
            print(s1, s2)

            if len(s1 & s2) > 0:
                overlaps += 1
    
    print(overlaps)

overlap()