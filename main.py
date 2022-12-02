ROCK = 1
PAPER = 2
SCISSORS = 3
LOSE = 0
WIN = 6
TIE = 3
TIED_SCENARIOS = ["C Z", "A X", "B Y"]
WINNING_SCENARIOS = ["B Z", "A Y", "C X"]

def update_score(line):
    if line[2]== 'X':
        return ROCK
    elif line[2] == 'Y':
        return PAPER
    elif line[2] == 'Z':
        return SCISSORS

def get_winner(line):
    if line in TIED_SCENARIOS:
        return TIE
    elif line in WINNING_SCENARIOS:
        return WIN
    else:
        return LOSE

def get_choice(my_move, their_choice):
    if my_move == 'X'
    pass

my_score = 0

f = open("input.txt","r")
for line in f:
    their_choice = line[0]
    my_move = line[2]
    my_choice = get_choice(my_move, their_choice)
    line = line.strip()
    my_score += update_score(line)
    my_score += get_winner(line)
    

f.close()
print(my_score)
"""x = lose, y = draw, z = win"""
