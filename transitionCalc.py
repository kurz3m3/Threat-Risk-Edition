import numpy as np

die = [1,2,3,4,5,6]

# use a for loop for each die to count how many winning / losing combinations there are
winning_combo = 0
losing_combo = 0

combinations = []
for dice1 in die:
    for dice2 in die:
        for dice3 in die:
            for dice4 in die:
                combinations.append([dice1,dice2,dice3,dice4])

for combination in combinations:
    combination = list(combination)
    print(combination)
print("Length of Arr:")
print(len(combinations))