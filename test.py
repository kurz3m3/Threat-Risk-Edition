import itertools

def generate_dice_combinations(n, die):
    # Generate all combinations of `n` dice rolls
    return list(itertools.product(die, repeat=n))

die = [1, 2, 3, 4, 5, 6]
# For example, generate combinations for 4 dice rolls
n = 5
combinations = generate_dice_combinations(n, die)
for combination in combinations:
    print(combination)

# Number of winning combinations for Team A: 2590
# Number of winning combinations for Team D: 2429
# Number of neutral combinations: 2757
# Total combinations: 7776
