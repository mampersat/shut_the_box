import random
import pdb


def print_board(board):
    print("Current Board:")
    for i in range(len(board)):
        print(f"{i + 1}: {'X' if board[i] else i + 1}", end="  ")
    print("\n")


def roll_dice():
    return random.randint(1, 6), random.randint(1, 6)


def close_tiles(board, tile_numbers):
    for tile_number in tile_numbers:
        board[tile_number - 1] = False


def find_combinations(nums, target_sum):
    def backtrack(start, target, path):
        if target == 0:
            combinations.append(path[:])
            return
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue  # Skip duplicate elements to avoid duplicate combinations
            if nums[i] > target:
                continue
            path.append(nums[i])
            backtrack(i + 1, target - nums[i], path)
            path.pop()

    combinations = []
    nums.sort()  # Sorting the input list can help optimize the search
    backtrack(0, target_sum, [])
    # print(combinations)
    return combinations

#       _             _             _           
#      | |           | |           (_)          
#   ___| |_ _ __ __ _| |_ ___  __ _ _  ___  ___ 
#  / __| __| '__/ _` | __/ _ \/ _` | |/ _ \/ __|
#  \__ \ |_| | | (_| | ||  __/ (_| | |  __/\__ \
#  |___/\__|_|  \__,_|\__\___|\__, |_|\___||___/
#                              __/ |            
#                             |___/             

def most_tiles(choices):
    sort_by_len = sorted(choices, key=len)
    return sort_by_len[-1]

def fewest_tiles(choices):
    sort_by_len = sorted(choices, key=len)
    return sort_by_len[0]

def highest_tile(choices):
    preferred = [9, 8, 7, 6, 5, 4, 3, 2]
    for p in preferred:
        for choice in choices:
            if p in choice:
                return choice

def expirement(choices):
    # preserve sevens
    for choice in choices:
        if choice[0] + choice[-1] != 7:
            return choice
        else:
            return highest_tile(choices)
        
def adaptive_strategy(choices):
    # Prioritize fewer tiles when few moves remain to increase win likelihood
    # Prefer high tiles early, shift to fewest tiles as game progresses
    if len(choices[0]) > 2:  # If multiple tiles are needed, prioritize high ones
        return most_tiles(choices)
    else:  # Near the end, prioritize fewer tiles or lower sums
        return fewest_tiles(choices)
    
def prioritize_low_high(choices):
    """
    The "Prioritize Low High" strategy:
    - If there are many combinations available (suggesting more tiles are still open),
      it uses the "Fewest Tiles" strategy to close smaller tiles.
    - If there are only a few combinations available (suggesting fewer open tiles),
      it uses the "Highest Tile" strategy to prioritize closing higher tiles.
    """
    if len(choices[0]) > 2:  # When there are still multiple open tiles, close fewer tiles.
        return fewest_tiles(choices)
    return highest_tile(choices)  # When fewer tiles are left, close higher ones.




def random_tiles(choices):
    return random.choices(choices)[0]


def play(strategy):
    board = [
        True
    ] * 9  # True represents an open tile, and False represents a closed tile

    # print("Welcome to Shut the Box!")
    # print_board(board)

    choices = True

    while choices and any(board):
        # input("Press Enter to roll the dice...")
        dice1, dice2 = roll_dice()
        # print(f"You rolled: {dice1} and {dice2}")

        available_tiles = [i + 1 for i in range(len(board)) if board[i]]
        # print("Available Tiles:", available_tiles)

        total_roll = dice1 + dice2
        # Find all possible choices
        choices = find_combinations(available_tiles, total_roll)

        if choices:
            if len(choices) == 1:
                chosen_tiles = choices[0]
            else:
                chosen_tiles = strategy(choices)

            # print(f"{chosen_tiles=}")

            close_tiles(board, chosen_tiles)
            # print(f"Tiles {chosen_tiles} closed!")

            # print_board(board)

    return not any(board)


def main():
    iterations = 100_000

    stratagies = [random_tiles, highest_tile, fewest_tiles, most_tiles, expirement, adaptive_strategy, prioritize_low_high]

    for stratagy in stratagies:
        wins = 0
        print(f"stratagy: {stratagy.__name__}")
        for i in range(iterations):
            wins += play(stratagy)

        # report strategy win rate  as a percentage
        print(f"Win Rate: {wins / iterations * 100:.2f}%")      

        # report stratey win rate as number of times you have to play to expect a win
        print(f"Win Rate: {1 / (wins / iterations):.0f} games\n")  
if __name__ == "__main__":
    main()
