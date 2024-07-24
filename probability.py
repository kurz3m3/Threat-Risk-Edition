import numpy as np

# def att_probability(sides, power):
#     # probability that ATT wins if DEF rolls 1-6
#     winprob = [5/6, 4/6, 3/6, 2/6, 1/6, 0]
#
#
#     total = pow(sides, power)

# create an array with possible die-roll results. (ints 1 thru 6)
die = [1, 2, 3, 4, 5, 6]  # this is the sides of our dice

# define number N of dice rolls to execute:
attacking_armies = 0
defensive_armies = 0
attacking_dice = 1
defending_dice = 1


# Running process P: rolling N dice ONE TIME
# def roll(die, num_dice):
#     rolls = np.random.choice(die, num_dice)
#     # data type that np.random.choice returns
#     return [rolls]  # this returns both the actual rolls as well as their sum
#
#
# print(roll(die, num_dice))

def append_results(data_array, item):
    if not data_array or len(data_array[-1]) == 6:
        data_array.append([])  # Create a new row if the last row is full or if the array is empty
    data_array[-1].append(item)  # Append the new item to the last row

# ------------------------------------------------------------------------------------------------

# !!!! TO-DO: RECOGNIZE WHO'S DICE IS WHOS ...
# Currently scales as if all dice are going to attack,
# meaning we have probabilities for: 1A 1D, 2A 1D, and 3A 1D
# and we need: 1A 2D (max clause? change if? L23), 2A 2D, and 3A 2D (change if?)

# number of dice in play
attackDice = 1
defendDice = 1

# len(faces)-sided die with each element representing the face's val
faces = [1, 2, 3, 4, 5, 6]

print(21 / 36)  # ... 15/36 = Ap ... control probability of DEF win w/ 2 dice
print(91 / 216)  # ... 125/216 = Ap ... control probability of DEF win w/ 3 dice (2A - 1D)
print(449 / 1296)  # ... 847/1296 = Ap ... control probability of DEF win w/ 4 dice (3A - 1D)

def dicePair(attDice, defDice, die):
    # calc
    numDice = attDice + defDice
    outcomes = 0
    for row in range(len(die)):
        # insert more def clause
        if numDice <= 2:
            for col in range(len(die)):
                if col <= row:
                    outcomes += 1
        elif numDice > 2:
            # scales the initial probability to an increased # of dice
            # formula to find DEF probability (RELIABLE)
            outcomes += pow(row + 1, numDice - 1)

    # total possible roll combos for any # of dice
    total = pow(len(die), numDice)

    # defender win prob, attacker win prob (as percentages)
    return(f"DEF Win Probability ({defDice} Dice): {round((outcomes / total) * 100, 2)}%",
           f"ATT Win Probability ({attDice} Dice): {round(((total - outcomes) / total) * 100, 2)}%")

print(dicePair(attackDice, defendDice, faces))
