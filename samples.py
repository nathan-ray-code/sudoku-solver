# these are downloaded Sudoku puzzles that possess varying degrees of difficulty to test the accuracy of our algorithm

# sudoku-solver.py imports the RandomPuzzle class created in this file to give the user an option to choose which difficulty he or she would like to see 
# the algorithm perform. Currently these are the sudoku puzzles broken down by their difficulty:
"""
    ------------------------------------------------------------------------------------
     Number of each difficulty:
    ------------------------------------------------------------------------------------
    1. Easy puzzles = 5         (sudoku_01, sudoku_02, sudoku_03, sudoku_04, sudoku_05)
    2. Medium puzzles = 5       (sudoku_06, sudoku_07, sudoku_08, sudoku_09, sudoku_10)
    3. Hard puzzles = 4         (sudoku_11, sudoku_12, sudoku_13, sudoku_14)
    4. Extra Hard puzzles = 2   (sudoku_17, sudoku_19)
    ------------------------------------------------------------------------------------

"""

import random

class RandomPuzzle:

    sudoku_01 = [
        [0, 7, 0, 0, 2, 0, 0, 4, 6],
        [0, 6, 0, 0, 0, 0, 8, 9, 0],
        [2, 0, 0, 8, 0, 0, 7, 1, 5],
        [0, 8, 4, 0, 9, 7, 0, 0, 0],
        [7, 1, 0, 0, 0, 0, 0, 5, 9],
        [0, 0, 0, 1, 3, 0, 4, 8, 0],
        [6, 9, 7, 0, 0, 2, 0, 0, 8],
        [0, 5, 8, 0, 0, 0, 0, 6, 0],
        [4, 3, 0, 0, 8, 0, 0, 7, 0]
    ]

    sudoku_02 = [
        [0, 0, 4, 0, 5, 0, 0, 0, 0],
        [9, 0, 0, 7, 3, 4, 6, 0, 0],
        [0, 0, 3, 0, 2, 1, 0, 4, 9],
        [0, 3, 5, 0, 9, 0, 4, 8, 0],
        [0, 9, 0, 0, 0, 0, 0, 3, 0],
        [0, 7, 6, 0, 1, 0, 9, 2, 0],
        [3, 1, 0, 9, 7, 0, 2, 0, 0],
        [0, 0, 9, 1, 8, 2, 0, 0, 3],
        [0, 0, 0, 0, 6, 0, 1, 0, 0]
    ]

    sudoku_03 = [
        [8, 0, 6, 0, 1, 0, 0, 0, 0],
        [0, 0, 3, 0, 6, 4, 0, 9, 0],
        [9, 0, 0, 0, 0, 0, 8, 1, 6],
        [0, 8, 0, 3, 9, 6, 0, 0, 0],
        [7, 0, 2, 0, 4, 0, 3, 0, 9],
        [0, 0, 0, 5, 7, 2, 0, 8, 0],
        [5, 2, 1, 0, 0, 0, 0, 0, 4],
        [0, 3, 0, 7, 5, 0, 2, 0, 0],
        [0, 0, 0, 0, 2, 0, 1, 0, 5]
    ]

    sudoku_04 = [
        [3, 8, 0, 9, 0, 0, 2, 0, 5],
        [0, 0, 0, 0, 0, 8, 7, 3, 0],
        [0, 6, 0, 3, 0, 0, 9, 8, 0],
        [0, 0, 0, 0, 0, 3, 5, 0, 1],
        [9, 1, 0, 5, 0, 7, 0, 2, 3],
        [7, 0, 3, 1, 0, 0, 0, 0, 0],
        [0, 3, 5, 0, 0, 1, 0, 9, 0],
        [0, 7, 4, 6, 0, 0, 0, 0, 0],
        [8, 0, 1, 0, 0, 2, 0, 6, 7]
    ]

    sudoku_05 = [
        [6, 0, 0, 0, 0, 9, 0, 0, 4],
        [0, 8, 9, 5, 0, 0, 0, 1, 6],
        [5, 0, 0, 0, 6, 0, 3, 0, 9],
        [8, 3, 1, 0, 0, 0, 7, 0, 5],
        [0, 2, 0, 0, 0, 0, 0, 6, 0],
        [9, 0, 7, 0, 0, 0, 8, 4, 2],
        [2, 0, 6, 0, 1, 0, 0, 0, 8],
        [3, 7, 0, 0, 0, 6, 9, 2, 0],
        [1, 0, 0, 3, 0, 0, 0, 0, 7]
    ]

    sudoku_06 = [
        [5, 0, 7, 2, 0, 0, 0, 9, 0],
        [0, 0, 6, 0, 3, 0, 7, 0, 1],
        [4, 0, 0, 0, 0, 0, 0, 6, 0],
        [1, 0, 0, 4, 9, 0, 0, 0, 7],
        [0, 0, 0, 5, 0, 8, 0, 0, 0],
        [8, 0, 0, 0, 2, 7, 0, 0, 5],
        [0, 7, 0, 0, 0, 0, 0, 0, 9],
        [2, 0, 9, 0, 8, 0, 6, 0, 0],
        [0, 4, 0, 0, 0, 9, 3, 0, 8]
    ]

    sudoku_07 = [
        [2, 0, 0, 0, 0, 0, 6, 9, 0],
        [0, 5, 0, 0, 0, 3, 0, 0, 0],
        [1, 7, 0, 0, 0, 9, 4, 0, 5],
        [0, 0, 3, 0, 2, 5, 0, 1, 8],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [7, 2, 0, 3, 8, 0, 5, 0, 0],
        [5, 0, 2, 6, 0, 0, 0, 4, 1],
        [0, 0, 0, 5, 0, 0, 0, 7, 0],
        [0, 6, 7, 0, 0, 0, 0, 0, 3]
    ]

    sudoku_08 = [
        [1, 5, 0, 2, 0, 9, 0, 0, 4],
        [0, 4, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 6, 3],
        [0, 7, 0, 0, 0, 0, 8, 0, 6],
        [6, 0, 0, 0, 0, 0, 0, 0, 5],
        [2, 0, 8, 0, 0, 0, 0, 1, 0],
        [4, 6, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 7, 0],
        [8, 0, 0, 5, 0, 1, 0, 4, 9]
    ]

    sudoku_09 = [
        [3, 4, 0, 0, 6, 0, 2, 0, 9],
        [2, 0, 8, 4, 9, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 3, 1, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 2, 5, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 5, 1, 4, 0, 3],
        [4, 0, 3, 0, 7, 0, 0, 6, 8]
    ]

    sudoku_10 = [
        [0, 2, 6, 0, 3, 0, 0, 0, 8],
        [9, 0, 0, 6, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 9, 0, 4, 0],
        [0, 0, 7, 3, 0, 2, 0, 0, 0],
        [0, 0, 4, 0, 7, 0, 8, 0, 0],
        [0, 0, 0, 8, 0, 6, 7, 0, 0],
        [0, 5, 0, 7, 2, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 5, 0, 0, 4],
        [4, 0, 0, 0, 6, 0, 2, 1, 0]
    ]

    sudoku_11 = [
        [0, 0, 6, 5, 0, 0, 0, 0, 8],
        [0, 9, 5, 0, 0, 0, 0, 2, 0],
        [7, 0, 0, 9, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 4, 0, 2, 7, 0],
        [0, 0, 0, 8, 7, 3, 0, 0, 0],
        [0, 7, 9, 0, 5, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 8, 0, 0, 9],
        [0, 5, 0, 0, 0, 0, 8, 1, 0],
        [3, 0, 0, 0, 0, 5, 4, 0, 0]
    ]

    sudoku_12 = [
        [0, 9, 1, 0, 7, 0, 0, 0, 0],
        [2, 0, 3, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 4, 0, 2, 9, 0, 7],
        [0, 0, 2, 8, 0, 6, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 1, 0, 4, 6, 0, 0],
        [1, 0, 5, 2, 0, 7, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 5, 0, 1],
        [0, 0, 0, 0, 1, 0, 7, 6, 0]
    ]

    sudoku_13 = [
        [0, 0, 2, 7, 8, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 9, 8, 0, 1],
        [4, 0, 0, 0, 0, 3, 0, 7, 0],
        [9, 0, 5, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 4, 0, 8],
        [0, 6, 0, 4, 0, 0, 0, 0, 7],
        [3, 0, 9, 8, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 3, 1, 6, 0, 0]
    ]

    sudoku_14 = [
        [0, 8, 7, 3, 0, 4, 0, 0, 0],
        [0, 3, 0, 5, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 2, 4, 5, 0],
        [0, 9, 6, 0, 1, 0, 8, 3, 0],
        [0, 2, 5, 8, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 7, 0, 1, 0],
        [0, 0, 0, 2, 0, 1, 7, 6, 0]
    ]

    sudoku_17 = [
        [0, 9, 6, 0, 0, 8, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 9, 0, 2, 0, 8, 0],
        [0, 5, 7, 8, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 9, 1, 6, 0],
        [0, 2, 0, 3, 0, 5, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 2, 0, 0, 5, 9, 0]
    ]

    sudoku_19 = [
        [0, 0, 0, 8, 0, 0, 9, 0, 0],
        [0, 9, 0, 0, 7, 0, 0, 0, 4],
        [0, 8, 4, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 4, 1, 0, 2, 0, 0],
        [0, 0, 3, 0, 0, 0, 5, 0, 0],
        [0, 0, 1, 0, 6, 9, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 7, 4, 0],
        [9, 0, 0, 0, 2, 0, 0, 3, 0],
        [0, 0, 7, 0, 0, 6, 0, 0, 0]
    ]

    easy_collection = [sudoku_01, sudoku_02, sudoku_03, sudoku_04, sudoku_05]
    medium_collection = [sudoku_06, sudoku_07, sudoku_08, sudoku_09, sudoku_10]
    hard_collection = [sudoku_11, sudoku_12, sudoku_13, sudoku_14]
    extra_hard_collection = [sudoku_17, sudoku_19] # MIGHT HAVE TO REMOVE THIS ONE IF IT'S PERFORMANCE DOES NOT IMPROVE!

    easy_rand = random.choice([0,1,2,3,4])
    easy_puzzle_board = easy_collection[easy_rand]

    medium_rand = random.choice([0,1,2,3,4])
    medium_puzzle_board = medium_collection[medium_rand]

    hard_rand = random.choice([0,1,2,3])
    hard_puzzle_board = hard_collection[hard_rand]

    extra_hard_rand = random.choice([0,1])
    extra_hard_puzzle_board = extra_hard_collection[extra_hard_rand]







