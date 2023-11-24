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


def make_choice(choices):
    # if only one choice, just return it
    if len(choices) == 1:
        return choices[0]

    # get rid of low value tiles in this order 2, 3, 4, 9, 5, 7, 8, 6
    for choice in choices:
        if 2 in choice:
            return choice
        if 3 in choice:
            return choice
        if 4 in choice:
            return choice
        if 9 in choice:
            return choice
        if 5 in choice:
            return choice
        if 7 in choice:
            return choice
        if 8 in choice:
            return choice
        if 6 in choice:
            return choice

    print("got this far... hmmm...")
    return choice[0]

    # if one choice is fewer tiles then next choice, pick it
    sort_by_len = sorted(choices, key=len)
    choice1 = sort_by_len[0]
    choice2 = sort_by_len[1]
    if len(choice1) < len(choice2):
        return choice1

    # most tiles
    # 1%
    sort_by_len = sorted(choices, key=len)
    return sort_by_len[-1]

    # fewest tiles
    # 7%
    sort_by_len = sorted(choices, key=len)
    return sort_by_len[0]

    # last choice... fewest tiles?
    # 6%
    return choices[-1]

    # Compare last two choices, pick one with out a 7
    # 4.5%
    choice1 = choices[-1]
    choice2 = choices[-2]
    if 7 in choice1:
        return choice2
    else:
        return choice1

    # last choice... fewest tiles?
    # 6%
    return choices[-1]

    # first choice... most tiles closed?
    # 1%
    # return choices[0]

    # random choice
    # 2%
    return random.choices(choices)[0]


def play():
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
            chosen_tiles = make_choice(choices)

            # print(f"{chosen_tiles=}")

            close_tiles(board, chosen_tiles)
            # print(f"Tiles {chosen_tiles} closed!")

            # print_board(board)

    return not any(board)


def main():
    wins = 0
    iterations = 1_000_000
    for i in range(iterations):
        wins += play()

    print(wins / iterations * 100)


if __name__ == "__main__":
    main()
