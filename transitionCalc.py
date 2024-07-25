import numpy as np

# Initialize the die faces
die = [1, 2, 3, 4, 5, 6]

# Generate all possible combinations of four dice rolls
combinations = []
for dice1 in die:
    for dice2 in die:
        for dice3 in die:
            for dice4 in die:
                for dice5 in die:
                    combinations.append([dice1, dice2, dice3, dice4, dice5])

# Initialize counters
team_A_wins = 0
team_D_wins = 0
ties = 0

# Iterate through each combination
for combination in combinations:
    # Split into teams
    dice1, dice2, dice3, dice4, dice5 = combination

    greatest_defense = 0
    greatest_attack = 0

    second_greatest_defense = 0
    second_greatest_attack = 0

    third_greatest_attack = 0

    # defense dice check
    if (dice1 >= dice2):
        greatest_defense = dice1
        second_greatest_defense = dice2
    else:
        greatest_defense = dice2
        second_greatest_defense = dice1

    # attack dice check
    if (dice3 >= dice4 and dice3 >= dice5):
        greatest_attack = dice3
        if (dice4 >= dice5):
            second_greatest_attack = dice4
            third_greatest_attack = dice5
        else:
            second_greatest_attack = dice5
            third_greatest_attack = dice4
    elif (dice4 >= dice5 and dice4 >= dice3):
        greatest_attack = dice4
        if (dice5 >= dice3):
            second_greatest_attack = dice5
            third_greatest_attack = dice3
    else:
        greatest_attack = dice5
        if (dice3 >= dice4):
            second_greatest_attack = dice3
            third_greatest_attack = dice4
        else:
            second_greatest_attack = dice4
            third_greatest_attack = dice3

    if ((greatest_attack > greatest_defense) and (second_greatest_defense >= second_greatest_attack) or (
            greatest_defense >= greatest_attack) and (second_greatest_attack > second_greatest_defense)):
        ties += 1
    elif ((greatest_defense >= greatest_attack) and (second_greatest_defense >= second_greatest_attack)):
        team_D_wins += 1
    elif ((greatest_defense < greatest_attack) and (second_greatest_defense < second_greatest_attack)):
        team_A_wins += 1

# Print the results
print("Number of winning combinations for Team A:", team_A_wins)
print("Number of winning combinations for Team D:", team_D_wins)
print("Number of neutral combinations:", ties)
print("Total combinations:", len(combinations))
