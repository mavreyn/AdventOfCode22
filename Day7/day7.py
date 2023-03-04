# Part 1 I literally have to rebuild the directory AHHHHHH
import re
from collections import deque

# I need to be able to make item objects
class Item:
    contains = []
    name = ''
    size = 0
    parent = None

    def __init__(self, name, parent, size=0):
        self.name = name
        self.parent = parent
        self.size = size
    
    def __str__(self):
        return 'child of ' + str(self.parent) + self.name + ' with size ' + str(self.size) + ' contains ' + str(len(self.contains)) + ' elements'


def main():
    with open('ex.txt') as f:
        # Get terminal input, start at /
        term = deque([l.strip('\n') for l in f.readlines()])
        term.popleft()

        print(term)
        
        root = Item('/', None)
        cd = root

        # Read line by line and never go back
        while term:
            cmd = term.popleft().split()
            print(cmd)

            # If $, take an action
            if cmd == ['$', 'ls']:
                while term[0][0] != '$':
                    cmd = term.popleft().split()
                    print(cmd)

                    # Add file or dir to current directory
                    if cmd[0] == 'dir':
                        cd.contains.append(Item(cmd[1], cd))
                        print(cd.contains)
                    else:
                        cd.contains.append(Item(cmd[1], cd, cmd[0]))

                    
            elif cmd[0] == '$' and cmd[1] == 'cd':
                if cmd[2] == '..':
                    cd = cd.parent
                else:
                    for item in cd.contains:
                        if item.name == cmd[2]:
                            cd = item
            
            print(cd)



if __name__ == '__main__':
    main()