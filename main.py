ROCK = 1
PAPER = 2
SCISSORS = 3
LOSE = 0
WIN = 6
TIE = 3
TIED_SCENARIOS = ["C Z", "A X", "B Y"]
WINNING_SCENARIOS = ["B Z", "A Y", "C X"]
"""A for Rock, B for Paper, and C for Scissors"""
def lose(their_choice):
    if their_choice == "A":
        return SCISSORS
    elif their_choice == 'B':
        return ROCK
    else:
        return PAPER
    

def win(their_choice):
    if their_choice == "A":
        return PAPER
    elif their_choice == 'B':
        return SCISSORS
    else:
        return ROCK

def tie(their_choice):
    if their_choice == "A":
        return ROCK
    elif their_choice == 'B':
        return PAPER
    else:
        return SCISSORS

def update_score(line):
    if line[2]== 'X':
        return ROCK
    elif line[2] == 'Y':
        return PAPER
    elif line[2] == 'Z':
        return SCISSORS


def get_score(my_move, their_choice):
    if my_move == 'X': 
        return LOSE + lose(their_choice)
    elif my_move == "Y":
        return TIE + tie(their_choice)
    else:
        return WIN + win(their_choice)
    

my_score = 0

f = open("input.txt","r")
for line in f:
    their_choice = line[0]
    my_move = line[2]
    my_score += get_score(my_move, their_choice)
    

f.close()
print(my_score)
