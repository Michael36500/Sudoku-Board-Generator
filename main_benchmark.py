#Made by Alex
#Special thanks to the answer by Alain T in this post https://stackoverflow.com/questions/45471152/how-to-create-a-sudoku-puzzle-in-python

#======Libraries======
import random
import copy
import save_board
import cv2
import time
#======Functions======
#Text on startup
def introduction():
    pass
    # print("Sudoku!\n")

    # print('''Rules:
    # 1) Each mini-board has to contain the symbols 1-9.
    # 2) Each symbol can only appear once in a row, column, or mini-board.''')

#Formula to validate sudoku pattern
def validate(x, y):
    offsets = (3 * (x % 3) + x // 3 + y) % 9 # Calculates the offsets so the numbers fit on a valid 9x9 Sudoku puzzle
    return offsets

#Prints board to the screen
def printBoard(board):
    pass
    #Variables
    # horizontal_line = "- - - - - - - - - - -"

    # # Preprocess the rows to add the vertical column separations
    # for row in board:
    #     for c in range(len(row)):
    #         if row[c] == 0: # if a cell has not been revealed, replace the present 0 with a space
    #             row[c] = " "
    #     row.insert(3, "|") # add the left vertical column
    #     row.insert(7, "|") # add the right vertical column

    # # Add the horizontal lines
    # board.insert(3, [horizontal_line]) # add the upper horizontal line
    # board.insert(7, [horizontal_line]) # add the lower horizontal line
    
    # # Print the board
    # for r in board:
    #     print(*r, end = " ") # print the row list, with it's elements separated by spaces
    #     print() # spacer

#======Main======
def main(a):
    #Variables
    board = [] # Main board
    rows = [] # Horizontal
    cols = [] # Vertical
    cells = random.sample(range(1, 10), 9) # Unique range of elements to create cells in each row

    #Enter Input Loop
    while True:
        #Difficulty Input
        try:
            # difficulty = float(input("Enter a difficulty (1-99): "))
            difficulty = float(60)

            #Bad inputs
            if difficulty < 0:
                raise Exception("Difficulty cannot be negative!")
            elif difficulty == 0:
                raise Exception("Difficulty cannot be 0!")
            elif difficulty > 99:
                raise Exception("Difficulty cannot be more than 99!")
            elif difficulty.is_integer() == False:
                raise Exception("Difficulty cannot be floating point values.")
        #Error handling (general)
        except ValueError:
            print("Difficulty must be an integer value.\n")
        #Error handling (specific)
        except Exception as specificError:
            print(specificError, end = "\n\n")
        #Exit Input Loop
        else:
            difficulty = int(difficulty)
            # print()
            break

    #Parent Row
    for row in random.sample(range(3), 3): # Loops through a random range of 3 numbers
        for r in random.sample(range(3), 3): # Loops through another random range of 3 numbers, effectively multiplying by 3 and creating a whole row with 9 shuffled elements
            rows.append(r * 3 + row)
    #Parent Column
    for col in random.sample(range(3), 3): # Columns use the same method as the rows
        for c in random.sample(range(3), 3): # 9 elements in a column, all randomized
            cols.append(c * 3 + col)

    #Main Board
    for r in rows: # Building the main board
        rank = [] # Local variable to append each row later
        for c in cols: # Creating a plane
            rank.append(cells[validate(r, c)]) # Validate random cells in rank
        board.append(rank) # Append rank to the main board

    hidden_board = copy.deepcopy(board) # Deep copies list and creates the hidden board

    #Difficulty
    for rank in hidden_board:
        for cell in range(len(rank)): # Goes through each cell
            if random.randint(1, 100) <= difficulty: # Random chance for difficulty
                rank[cell] = 0 # "0" is a placeholder for nothing

    #Obstructed Board
    # printBoard(hidden_board)
    
    #Asks to save hidden board image
    while True:
        # response = input("Would you like to save the hidden board? (y/n): ").lower()
        response = "y"

        #If in answer is y, then save board, else skip
        if response == "y":
            save_board.save_board(hidden_board, "hidden_board{}".format(a))
        #Error
        elif response != "n":
            print("Input error.\n")
            continue
        break # Exit input loop

    # print("\nPress enter to see the full board.")

    # input()

    #Full Board
    # printBoard(board)

    #Asks to save full board image
    while True:
        # response = input("Would you like to save the full board? (y/n): ").lower()
        response = "y"

        #If in answer is y, then save board, else skip
        if response == "y":
            save_board.save_board(board, "full_board{}".format(a))
        #Error
        elif response != "n":
            print("Input error.\n")
            continue
        break # Exit input loop

#======Execution Check======
if __name__ == '__main__':
    introduction()
    bench = cv2.imread("benchmarking.png")
    plate = cv2.imread("bench_back.png")
    play = True

    # while(play):
    cv2.imshow("Benchmark", bench)
    cv2.waitKey(100)
    Start = time.time()
    for a in range(1000):
        # print() # Spacer

        main(a)
        # print() # Spacer

        #Enter Input Loop
        while True:
            # response = input("Would you like to play again (y/n): ").lower()
            response = "y"

            if response == "y":
                play = True
            elif response == "n":
                play = False
            #Error
            else:
                print("Input error.\n")
                continue
            break # Exit input loop
    Total = time.time() - Start
    print(Total)
    plate = cv2.putText(plate, str(Total), (30,400), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 6, (73, 177, 251), 2)
    cv2.imshow("Benchmark", plate)
    cv2.waitKey(0)