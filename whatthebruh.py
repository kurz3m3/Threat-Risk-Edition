import itertools
import random
import matplotlib.pyplot as plt

outcome_tracker = {'att': [], 'def': [], 'draw': []}

# ---------------- WIN COUNTER ZONE START ---------------------------------------------------------------------------- #
def win_counter(att_troops, outcomes_list):   # Determines how many outcomes each pos. wins based on # of dice in play
    att_win = 0
    def_win = 0
    draw = 0

    # Searches every outcome and compares the rolled "dice" inside to see who wins; first dice are ATT, followed by DEF
    for outcomes in outcomes_list:
        # num_troops represents the number of ATTacking dice/troops, as those come first.
        if att_troops == 1:
            if outcomes[0] == max(outcomes) and outcomes[0] not in outcomes[att_troops:]:   # if ATT dice is highest val
                att_win += 1   # in this case, there is 1ATT and 2+DEF, so def loses a troop but doesn't vanish
                outcome_tracker['att'].append(outcomes)   # saves outcome as a draw for result selection
            else:
                def_win += 1
                outcome_tracker['def'].append(outcomes)

        # Length of outcomes - num_troops = DEFending dice
        elif len(outcomes) - att_troops == 1:
            if outcomes[len(outcomes) - 1] == max(outcomes):   # if lone DEF dice is highest val, win
                def_win += 1   # in this case, there are 2+ATT and 1DEF, so att loses a troop but doesn't vanish
                outcome_tracker['def'].append(outcomes)
            else:
                att_win += 1
                outcome_tracker['att'].append(outcomes)

        else:
            outcomes = list(outcomes)
            att_max = outcomes.pop(outcomes.index(max(outcomes[:att_troops])))
            temp_att_troops = att_troops - 1   # THIS is because we removed an element so the size changed

            if att_max > max(outcomes[temp_att_troops:]) and max(outcomes[:temp_att_troops]) > min(outcomes[temp_att_troops:]):
                att_win += 1
                outcome_tracker['att'].append(outcomes)
            elif att_max <= max(outcomes[temp_att_troops:]) and max(outcomes[:temp_att_troops]) <= min(outcomes[temp_att_troops:]):
                def_win += 1
                outcome_tracker['def'].append(outcomes)
            else:
                draw += 1   # both sides lose a troop
                outcome_tracker['draw'].append(outcomes)

            outcomes.insert(0, att_max)
            outcomes = tuple(outcomes)

    return "Att Wins: ", att_win, "Def Wins: ", def_win, "Draws: ", draw

# ---------------- WIN COUNTER ZONE END ------------------------------------------------------------------------------ #

# ---------------- PROB CALC ZONE START ------------------------------------------------------------------------------ #

# def probability_calculator(outcomes_list):
#   print(f"Probability that {team} wins with {attackers} troops versus {defenders} troops: ")
#     total = len(outcomes_list)
#     return x / total

# ---------------- PROB CALC ZONE END -------------------------------------------------------------------------------- #

# ---------------- USER INTERACTION ZONE START ----------------------------------------------------------------------- #

# Initialize the die faces
die = [1, 2, 3, 4, 5, 6]

# The user selects # of attacking troops and defending troops
attackers = int(input("Enter Number of Attacking Troops: "))
defenders = int(input("Enter Number of Defending Troops: "))

# count out how many dice based on # attacking troops
att_dice = 3 if attackers > 3 else attackers
def_dice = 2 if defenders > 2 else defenders

def generate_dice_combinations(n, dice):
    # Generate all combinations of `n` dice rolls
    return list(itertools.product(dice, repeat=n))

# Generate all possible combinations of four dice rolls
combinations = generate_dice_combinations(att_dice + def_dice, die)
win_counter(att_dice, combinations)

# while loop until att is 0 or def is 0 where we keep prompting to battle again or quit... before prompt, call probcalc
# once press battle we **pick a random outcome from our outcome bank and then tell them if they won or not** + who died
turns = 0
while attackers != 0 and defenders != 0:
    # - probcalc (all the way to 0)

    # - "simulating fight"
    print("Simulating fight between ATT and DEF ... ")

    # - random_element = random.choice(my_list)
    result = random.choice(combinations)

    if result in outcome_tracker['att']:
        defenders -= 1
        print('ATT Win - 1 DEF Troop Lost')
    if result in outcome_tracker['def']:
        attackers -= 1
        print('DEF Win - 1 ATT Troop Lost')
    if result in outcome_tracker['draw']:
        defenders -= 1
        attackers -= 1
        print('DRAW - 1 DEF and 1 ATT Troop Lost')

    turns += 1
    print(f"{attackers} ATT Troops Remaining, {defenders} DEF Troops Remaining")

if attackers == 0:
    print(f"DEF Won in {turns} turns!")
elif defenders == 0:
    print(f"ATT Won in {turns} turns!")

# ---------------- USER INTERACTION ZONE END ------------------------------------------------------------------------- #

