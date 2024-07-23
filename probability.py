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
num_dice = 2  # because we are rolling three dice in this initial question


# Running process P: rolling N dice ONE TIME
def roll(die, num_dice):
    rolls = np.random.choice(die, num_dice)
    sum = np.ndarray.sum(rolls)  # we need a special sum function because of the
    # data type that np.random.choice returns

    return [rolls, sum]  # this returns both the actual rolls as well as their sum

print(roll(die, num_dice))
