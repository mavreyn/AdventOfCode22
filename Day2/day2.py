# Part 1 RPS calculate winning score
SCORES_1 = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

STATES_1 = {
    'A X': 3,
    'B Y': 3,
    'C Z': 3,

    'A Y': 6,
    'B Z': 6,
    'C X': 6,

    'A Z': 0,
    'B X': 0,
    'C Y': 0,
}

def RPS_score():
    curr_score = 0

    with open('Re.txt') as f:
        for line in f:
            # Add score for symbol and state
            curr_score += SCORES_1[line[2]] + STATES_1[line[:3]]
    
    print(curr_score)



# Part 2 making the game go according to plan
SYMBOLS = ['A', 'B', 'C']

# Auxiliary functions
def win(s):
    return SYMBOLS[SYMBOLS.index(s) - 2]

def lose(s):
    return SYMBOLS[SYMBOLS.index(s) - 1]

SCORES_2 = {
    'A': 1,
    'B': 2,
    'C': 3,
}

SCORES_GAME = {
    'X': 0,
    'Y': 3,
    'Z': 6,
}

def RPS_choosen_end():
    curr_score = 0

    with open('Re.txt') as f:
        for line in f:
            # symbol score
            key = ''

            if line[2] == 'X':
                key = lose(line[0])
            elif line[2] == 'Y':
                key = line[0]
            else:
                key = win(line[0])

            # add with game result score
            curr_score += SCORES_2[key] + SCORES_GAME[line[2]]

    print(curr_score)

RPS_choosen_end()