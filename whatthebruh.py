import itertools
import random

# ---------------- WIN COUNTER ZONE START ---------------------------------------------------------------------------- #
def win_counter(num_troops, outcomes_list):   # Determines how many outcomes each pos. wins based on # of dice in play
    att_win = 0
    def_win = 0
    no_win = 0

    # Searches every outcome and compares the rolled "dice" inside to see who wins; first dice are ATT, followed by DEF
    for outcomes in outcomes_list:
        # num_troops represents the number of ATTacking dice/troops, as those come first.
        if num_troops == 1:
            if outcomes[0] > max(outcomes[num_troops:]):   # if lone ATT dice is highest val, win
                if len(outcomes) - num_troops == 1:
                    att_win += 1
                else:
                    no_win += 1   # in this case, there is 1ATT and 2DEF, so def loses a troop but doesn't vanish
            else:
                def_win += 1

        # Length of outcomes - num_troops = DEFending dice
        elif len(outcomes) - num_troops == 1:
            if outcomes[len(outcomes) - 1] >= max(outcomes[:num_troops]):   # if lone DEF dice is highest val, win
                if num_troops == 1:
                    def_win += 1
                else:
                    no_win += 1   # in this case, there are 2ATT and 1DEF, so att loses a troop but doesn't vanish
            else:
                att_win += 1

        else:
            if max(outcomes[:num_troops]) > max(outcomes[num_troops:]) and min(outcomes[:num_troops]) > min(outcomes[num_troops:]):
                att_win += 1
            elif max(outcomes[:num_troops]) <= max(outcomes[num_troops:]) and min(outcomes[:num_troops]) <= min(outcomes[num_troops:]):
                def_win += 1
            else:
                no_win += 1   # both sides lose a troop

    return att_win, def_win, no_win

# ---------------- WIN COUNTER ZONE END ------------------------------------------------------------------------------ #

# ---------------- PROB CALC ZONE START ------------------------------------------------------------------------------ #

# def probability_calculator(outcomes_list):
#
#     total = len(outcomes_list)
#     return x / total

# ---------------- PROB CALC ZONE END -------------------------------------------------------------------------------- #

# ---------------- USER INTERACTION ZONE START ----------------------------------------------------------------------- #

# Initialize the die faces
die = [1, 2, 3, 4, 5, 6]

# The user selects # of attacking troops and defending troops
attackers = int(input("Enter Number of Attacking Troops: "))
defenders = int(input("Enter Number of Defending Troops: "))

def generate_dice_combinations(n, dice):
    # Generate all combinations of `n` dice rolls
    return list(itertools.product(dice, repeat=n))

# Generate all possible combinations of four dice rolls
combinations = generate_dice_combinations(attackers + defenders, die)
outcome_tracker = {'att',
                   'def',
                   'draw'}

print(win_counter(attackers, combinations))

# while loop until att is 0 or def is 0 where we keep prompting to battle again or quit... before prompt, call probcalc
# once press battle we **pick a random outcome from our outcome bank and then tell them if they won or not** + who died
# - while att not 0 and def not 0
# - probcalc (all the way to 0)
# - "simulating fight"
# - random_element = random.choice(my_list)
# - if (1,2,3,4) in att_dict.values():
# -    -1 def
# -    print('1 def die') AKA the defendingtroops var
# -    thisdict.update({"att": 2020})
# - if (1,2,3,4) in def_dict.values():
# -    -1 att
# -    print('1 att die')
# -    thisdict.update({"def": 2020})
# - if (1,2,3,4) in draw_dict.values():
# -    -1 def -1 att
# -    print('1 att die 1 def die')
# -    thisdict.update({"draw": 2020})

# ---------------- USER INTERACTION ZONE END ------------------------------------------------------------------------- #
