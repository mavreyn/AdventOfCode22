# Part 1 find how many trees are visible

import numpy as np

# How many trees are visible from the left of a 1d list
# How many elements are strictly increasing
# Preserves trees already visible
def count_vis(trees, prev):
    res = prev
    res[0] = True
    max = 0
    for i in range(len(trees)):
        if trees[i] > max:
            max = trees[i]
            res[i] = True
    
    return res



def visTrees():

    with open('re.txt') as f:
        # Start with line 1
        field = np.array([int(d) for d in f.readline().strip('\n')])


        for ln in f:
            # Use np.vstack for the rest
            treeln = [int(d) for d in ln.strip('\n')]
            field = np.vstack([field, treeln])

        nrow, ncol = field.shape
        vis = np.array([[False]*ncol for _ in range(nrow)])
            
        # Test in each direction
        for i in range(ncol):
            vis[:, i] = count_vis(field[:, i], vis[:, i])
            vis[::-1, i] = count_vis(field[::-1, i], vis[::-1, i])
        
        for j in range(nrow):
            vis[j, :] = count_vis(field[j, :], vis[j, :])
            vis[j, ::-1] = count_vis(field[j, ::-1], vis[j, ::-1])


        print(field)
        print(vis)

        # Find total amount that are True
        total = 0

        for x in vis:
            for y in x:
                if y:
                    total += 1
        
        print(total)

visTrees()