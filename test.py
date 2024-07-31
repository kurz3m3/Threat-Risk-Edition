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
    return rolls


def roll_defending(n):
    rolls = [random.choice(die) for _ in range(n)]
    return rolls


# Generate all possible combinations of four dice rolls
combinations = generate_dice_combinations(5)

# Initialize counters
team_A_wins = 0
team_D_wins = 0
ties = 0


# Iterate through each combination
def determine_outcomes(num_attack, num_defend):
    attack_rolls = roll_attacking(num_attack)
    defend_rolls = roll_defending(num_defend)
    if len(defend_rolls) == 2:
        dice1, dice2 = sorted([attack_rolls])
        print(dice1, dice2)
    else:
        dice1 = attack_rolls[0]
        print(dice1)

    if len(attack_rolls) == 3:
        dice3, dice4, dice5 = sorted([attack_rolls])
        print(dice3, dice4, dice5)
    elif len(attack_rolls) == 2:
        dice3, dice4 = sorted([attack_rolls])
        print(dice3, dice4)
    else:
        dice3 = attack_rolls[0]
        print(dice3)


print("TESTING")
determine_outcomes(3, 1)
determine_outcomes(2, 2)
determine_outcomes(1, 1)
# Number of winning combinations for Team A: 2590
# Number of winning combinations for Team D: 2429
# Number of neutral combinations: 2757
# Total combinations: 7776