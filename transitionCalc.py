import numpy as np
import itertools
import random

# Initialize the die faces
die = [1, 2, 3, 4, 5, 6]


def generate_dice_combinations(n):
    # Generate all combinations of `n` dice rolls
    return list(itertools.product(die, repeat=n))


def roll_attacking(n):
    rolls = [random.choice(die) for _ in range(n)]
    rolls = sorted(rolls, reverse=True)
    return rolls


def roll_defending(n):
    rolls = [random.choice(die) for _ in range(n)]
    rolls = sorted(rolls, reverse=True)
    return rolls


# Generate all possible combinations of four dice rolls
combinations = generate_dice_combinations(5)

# Initialize counters
team_A_wins = 0
team_D_wins = 0
ties = 0

# Iterate through each combination
def determine_outcomes(num_attack, num_defend):
    defense_win = 0
    attacking_win = 0
    tie = 0
    attack_rolls = roll_attacking(num_attack)
    defend_rolls = roll_defending(num_defend)
    if len(defend_rolls) == 2:
        dice1, dice2 = defend_rolls
    else:
        dice1 = defend_rolls[0]

    if len(attack_rolls) == 3:
        dice3, dice4, dice5 = attack_rolls
    elif len(attack_rolls) == 2:
        dice3, dice4 = attack_rolls
    else:
        dice3 = attack_rolls[0]

    if len(defend_rolls) == 2 and len(attack_rolls) >= 2:
        if dice1 >= dice3 and dice2 >= dice4:
            defense_win += 2
        elif dice3 > dice1 and dice4 > dice2:
            attacking_win += 2
        elif dice2 >= dice4 or dice1 >= dice3 and dice2 < dice4 or dice1 < dice3:
            tie += 1

    elif len(defend_rolls) >= 1 and len(attack_rolls) == 1:
        if dice1 >= dice3:
            defense_win += 1
        else:
            attacking_win += 1
    # returns either [(2/1/0),(2/1/0), (1/0)]
    return defense_win, attacking_win, tie



# Print the results
print("Number of winning combinations for Team A:", team_A_wins)
print("Number of winning combinations for Team D:", team_D_wins)
print("Number of neutral combinations:", ties)
print("Total combinations:", len(combinations))
