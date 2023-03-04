# Part 1 find start-of-packet marker
# Part 2 same procedure but change CHARS to 14 from 4

def rem_dup(l):
    ret = []
    [ret.append(c) for c in l if c not in ret]
    return ret

CHARS = 14

def sop():
    with open('re.txt') as f:
        l = f.read().strip('\n')

        # Loop through all combos
        i=CHARS
        curr_sop =list(l[i-CHARS:i])
        print(rem_dup(curr_sop))
        print(curr_sop)

        while curr_sop != rem_dup(curr_sop):
            i += 1
            curr_sop =list(l[i-CHARS:i])
        
        print(i)
        print(curr_sop)
        
      

sop()