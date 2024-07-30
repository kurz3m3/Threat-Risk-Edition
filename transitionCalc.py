import numpy as np
import matplotlib.pyplot as plt

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
# print("Number of winning combinations for Team A:", team_A_wins)
# print("Number of winning combinations for Team D:", team_D_wins)
# print("Number of neutral combinations:", ties)
# print("Total combinations:", len(combinations))

# Hard-coded ... Revise later
probabilities = {'A1D1->A1D0':15/36,
                 'A1D1->A0D1':21/36,
                 'A1D2->A1D1':55/216,
                 'A1D2->A0D2':161/216,
                 'A2D1->A2D0':125/216,
                 'A2D1->A1D1':91/216,
                 'A2D2->A2D0':295/1296,
                 'A2D2->A1D1':420/1296,
                 'A2D2->A0D2':581/1296,
                 'A3D1->A3D0':847/1296,
                 'A3D1->A2D1':449/1296,
                 'A3D2->A3D0':2590/7776,
                 'A3D2->A2D1':2757/7776,
                 'A3D2->A1D2':2429/7776}

# attacking_troops = input("Enter Number of Attacking Troops: ")
# defending_troops = input("Enter Number of Defending Troops: ")
# attacking_conquer_prob = 1
# defending_conquer_prob = 1
#
# # selection tree ... revise later
# while attacking_troops >= 3 and defending_troops >= 2:
#     attacking_conquer_prob *= probabilities[]
#     defending_conquer_prob *= probabilities[]
#
#
# team_selection = input("Who are you playing as?: ")
# if team_selection == "att":
#     print(f"Probability to conquer as ATTACKER with {attacking_troops} troops versus {defending_troops}: \n")
#     print()
# elif team_selection == "def":
#     print(f"Probability to conquer as DEFENDER with {defending_troops} troops versus {attacking_troops}: \n")
#     print()

# Define matrix parameters
attacker = 3
defender = 2
attacker_count = []
defender_count = []

for guy in range(1, attacker + 1):
    attacker_count.append(f"Attacker {guy}")
for other_guy in range(1, defender + 1):
    defender_count.append(f"Defender {other_guy}")


risk_matrix_values = np.array([
    [1, 2, 3],
    [2, 4, 6],
    [3, 6, 9],
    [4, 8, 12]
])

# Plotting the matrix
fig, ax = plt.subplots()
cax = ax.matshow(risk_matrix_values, cmap='YlOrBr')

# Add color bar
plt.colorbar(cax)

# Set labels
ax.set_xticks(np.arange(len(attacker_count)))
ax.set_yticks(np.arange(len(defender_count)))

plt.xlabel('Attacker Troops')
plt.ylabel('Defender Troops')
plt.title('Transition Matrix')

# Annotate each cell with the risk value
for i in range(len(risk_matrix_values[1])):
    for j in range(len(risk_matrix_values[0])):
        ax.text(j, i, str(risk_matrix_values[i, j]), va='center', ha='center')

plt.show()

[[]]