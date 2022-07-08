# Made by Michael36500

import cv2
# from tqdm import tqdm

# my idea here is to load predefined image of sudoku board and draw into it.
def save_board(board, name):
    # loads empty sudoku board into img
    img = cv2.imread("sudokuboard.png")
    # gap equals space between each number
    gap = 102
    actual_line = -18
    # for line in tqdm(board):
    for line in board:
        if "-" in str(line):
            pass
        else:
            actual_char = 25
            actual_line += gap
            for char in line:
                if char == "|":
                    continue
                if char != 0:    
                    cv2.putText(img, str(char), (actual_char, actual_line), cv2.FONT_HERSHEY_PLAIN, 5, (0,0,0), 5)
                actual_char += gap
    cv2.imwrite("{}.png".format(str(name)), img)
