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


wlArray = []
defendProb = 0
attackProb = 0
numDice = 2
totalOutcomes = pow(6, numDice)  # 6 to the power of how many dice we roll
# note: 0 to 6 = 0 to 5 =  1 to 6
for i in range(1): # this is supposed to start at 6^2 and continue to however many
    append_results(wlArray, [])
    for defend in range(0, 6):
        for attack in range(0, 6):
            if defend >= attack:
                append_results(wlArray, "L")
                defendProb += 1
            else:
                append_results(wlArray, "W")
                attackProb += 1

if numDice > 2:
    attackProb = attackProb * numDice

# we make a new list when doing over 36 grid so that we can have [wlwlwl] [wlwlwl] [wlkwlwlwl] (each dimension in cube)
# new total outcomes is 6^3 ... calculate the probability
# -----------------------------------------------------------------------
print("\nPrinting WL ARRAY:")
for row in wlArray:
    print(row)

# made variables so i can use fstrings
attackL = round((defendProb / totalOutcomes) * 100, 2)
attackW = round((attackProb / totalOutcomes) * 100, 2)

print("These are the probabilities that someone wins with 1 dice on each side: ")
print("Attack Loss: ", f"{attackL}%")
print("Attack Win: ", f"{attackW}%")
