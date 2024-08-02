import itertools
import random
import numpy as np

outcome_tracker = {'2att': [], 'att': [], '2def': [], 'def': [], 'draw': []}

def generate_dice_combinations(n, dice):
    # Generate all combinations of `n` dice rolls
    return list(itertools.product(dice, repeat=n))

# ---------------- WIN COUNTER ZONE START ---------------------------------------------------------------------------- #
def win_counter(att_troops, outcomes_list):   # Determines how many outcomes each pos. wins based on # of dice in play
    both_att_win = 0
    att_win = 0
    both_def_win = 0
    def_win = 0
    draw = 0

    # Searches every outcome and compares the rolled "dice" inside to see who wins; first dice are ATT, followed by DEF
    for outcomes in outcomes_list:
        # num_troops represents the number of ATTacking dice/troops, as those come first.
        if att_troops == 1:
            outcomes = list(outcomes)
            if outcomes[0] == max(outcomes) and outcomes[0] not in outcomes[att_troops:]:   # if ATT dice is highest val
                att_win += 1   # in this case, there is 1ATT and 2+DEF, so def loses a troop but doesn't vanish
                outcome_tracker['att'].append(outcomes)   # saves outcome as a draw for result selection
            else:
                def_win += 1
                outcome_tracker['def'].append(outcomes)

        # Length of outcomes - num_troops = DEFending dice
        elif len(outcomes) - att_troops == 1:
            outcomes = list(outcomes)
            if outcomes[len(outcomes) - 1] == max(outcomes):   # if lone DEF dice is highest val, win
                def_win += 1   # in this case, there are 2+ATT and 1DEF, so att loses a troop but doesn't vanish
                outcome_tracker['def'].append(outcomes)
            else:
                att_win += 1
                outcome_tracker['att'].append(outcomes)

        else:
            outcomes = list(outcomes)
            att_max_index = outcomes.index(max(outcomes[:att_troops]))
            att_max = outcomes.pop(outcomes.index(max(outcomes[:att_troops])))
            temp_att_troops = att_troops - 1   # THIS is because we removed an element so the size changed
            # things are being double counted
            if att_max > max(outcomes[temp_att_troops:]) and max(outcomes[:temp_att_troops]) > min(outcomes[temp_att_troops:]):
                both_att_win += 1   # since this is 2ATT and 2DEF minimum, 2 troops guaranteed to die
                outcomes.insert(att_max_index, att_max)
                outcome_tracker['2att'].append(outcomes)
            elif att_max <= max(outcomes[temp_att_troops:]) and max(outcomes[:temp_att_troops]) <= min(outcomes[temp_att_troops:]):
                both_def_win += 1   # since this is 2ATT and 2DEF minimum, 2 troops guaranteed to die
                outcomes.insert(att_max_index, att_max)
                outcome_tracker['2def'].append(outcomes)
            else:
                draw += 1   # both sides lose 1 troop
                outcomes.insert(att_max_index, att_max)
                outcome_tracker['draw'].append(outcomes)

    return "Att Wins: ", both_att_win + att_win, "Def Wins: ", both_def_win + def_win, "Draws: ", draw

# ---------------- WIN COUNTER ZONE END ------------------------------------------------------------------------------ #

# ---------------- PROB CALC ZONE START ------------------------------------------------------------------------------ #

# def probability_calculator(outcomes_list):
#   print(f"Probability that {team} wins with {attackers} troops versus {defenders} troops: ")
#     total = len(outcomes_list)
#     return x / total

# fill matrix with zeroes, then,
# loop win counter with 1-3 and 1-2 then fill matrix????

#        A0D0, A0D1, A0D2, A1D0, A1D1, A1D2, A2D0, A2D1, A2D2, A3D0, A3D1, A3D2
# A0D0 [[0,0,0,0,0,0,0,0,0,0,0,0],
# A0D1  [0,0,0,0,0,0,0,0,0,0,0,0],
# A0D2  [0,0,0,0,0,0,0,0,0,0,0,0],
# A1D0  [0,0,0,0,0,0,0,0,0,0,0,0],
# A1D1  [0,21/36,0,15/36,0,0,0,0,0,0,0,0],
# A1D2  [0,0,161/216,0,55/216,0,0,0,0,0,0,0],
# A2D0  [0,0,0,0,0,0,0,0,0,0,0,0],
# A2D1  [0,0,0,0,91/216,0,125/216,0,0,0,0,0],
# A2D2  [0,0,295/1296,0,420/1296,0,581/1296,0,0,0,0,0],
# A3D0  [0,0,0,0,0,0,0,0,0,0,0,0],
# A3D1  [0,0,0,0,0,0,0,441/1296,0,855/1296,0,0],
# A3D2  [0,0,0,0,0,0,2275/7776,2890/7776,0,2611/7776,0,0]]

risk = np.array([[0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0], [0,21/36,0,15/36,0,0,0,0,0,0,0,0], [0,0,161/216,0,55/216,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,91/216,0,125/216,0,0,0,0,0], [0,0,295/1296,0,420/1296,0,581/1296,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,441/1296,0,855/1296,0,0], [0,0,0,0,0,0,2275/7776,2890/7776,0,2611/7776,0,0]])
rounds = 1
transition_matrix = np.linalg.matrix_power(risk, rounds)
print(transition_matrix)

# ---------------- PROB CALC ZONE END -------------------------------------------------------------------------------- #

# ---------------- USER INTERACTION ZONE START ----------------------------------------------------------------------- #

# Initialize the die faces
die = [1, 2, 3, 4, 5, 6]

# The user selects # of attacking troops and defending troops
attackers = int(input("Enter Number of Attacking Troops: "))
defenders = int(input("Enter Number of Defending Troops: "))

# "absolute win" simulation
print("Legibility Note: First dice are attacking, last dice are defending")

turns = 0
while attackers > 0 and defenders > 0:
    # count out how many dice based on # of troops in play
    if attackers > 3:
        att_dice = 3
    else:
        att_dice = attackers
    if defenders > 2:
        def_dice = 2
    else:
        def_dice = defenders

    # Generate all possible combinations of relevant dice rolls
    combinations = list(generate_dice_combinations(att_dice + def_dice, die))

    # Calculates winning combinations according to # of dice in play
    win_counter(att_dice, combinations)

    # - "simulating fight"
    print("Simulating fight between ATT and DEF ... ")

    # - random_element = random.choice(my_list)
    result = list(random.choice(combinations))
    print(result)

    # - searches for result in of all outcomes for roll
    if result in outcome_tracker['att']:
        defenders -= 1
        print(' *** ATT Win - 1 DEF Troop Lost *** ')
    if result in outcome_tracker['2att']:
        defenders -= 2
        print(' *** ATT Win - 2 DEF Troop Lost *** ')
    if result in outcome_tracker['def']:
        attackers -= 1
        print(' *** DEF Win - 1 ATT Troop Lost *** ')
    if result in outcome_tracker['2def']:
        attackers -= 2
        print(' *** DEF Win - 2 ATT Troop Lost *** ')
    if result in outcome_tracker['draw']:
        defenders -= 1
        attackers -= 1
        print(' *** DRAW - 1 DEF and 1 ATT Troop Lost *** ')

    turns += 1
    print(f"{attackers} ATT Troops Remaining, {defenders} DEF Troops Remaining\n")

    # reset outcome tracker for next dice size
    outcome_tracker.clear()
    outcome_tracker = {'2att': [], 'att': [], '2def': [], 'def': [], 'draw': []}

if attackers == 0:
    print(f"DEF Won in {turns} turns!")
elif defenders == 0:
    print(f"ATT Won in {turns} turns!")

# ---------------- USER INTERACTION ZONE END ------------------------------------------------------------------------- #

