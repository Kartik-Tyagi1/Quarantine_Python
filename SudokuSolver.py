"""
1) Create a function to print a board
2) Create a fucntion to find an emtpy slot on the board
3) Create a function to fill an empty slot of the board
4) Create a function to determine if the inputted number is valid
5) If the number is valid is then continue else, go back and see if anything in the board is wrong
6) Use 3-4 to solve the entire board
"""

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

end_of_line = 8

def print_board(sudoku_board):
    """
    Function will print the board like an actual sudoku board
    Will put lines to separate board into 3x3 squares
    """
    for i in range(len(sudoku_board)):
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - - - ')

        for j in range(len(sudoku_board[0])):
            if j % 3 == 0 and j != 0:
                print(' | ', end="")

            if j == end_of_line:
                print(sudoku_board[i][j])
            else:
                print(str(sudoku_board[i][j]) + " " , end="")



def find_empty(sudoku_board):
    """
    Function will return the coordinate of empty place in the board in tuple form
    (row, col)
    """
    for i in range(len(sudoku_board)):
        for j in range(len(sudoku_board[0])):
            if sudoku_board[i][j] == 0:
                return (i, j)

    return None # There are no empty spaces


def valid_input(sudoku_board, input_num, position):
    # Step 1: Check if the number is valid based on the row
    for i in range(len(sudoku_board[0])):
        if sudoku_board[position[0]][i] == input_num and position[1] != i: # Second skips checking input postion
            return False

    # Step 2: Check if the number is valid based on the column
    for i in range(len(sudoku_board)):
        if sudoku_board[i][position[1]] == input_num and position[0] != i: # Second skips checking input postion
            return False

    # Step 3: Check if the number is valid based on the 3x3 square
    '''
    We are going to split the board into 3x3 squares and use a label system
    (0,0)   (0,1)   (0,2)
    (1,0)   (1,1)   (1,2)
    (2,0)   (2,1)   (2,2)
    
    To do this we will use integer division based on the position to find the box
    Keep in mind that the position variable is in (row,column) so it is like (y,x)
    When doing this check box_X will be the position[1] and box_Y will be position[0]
    '''

    box_X = position[1] // 3
    box_Y = position[0] // 3

    for i in range(box_Y*3 , box_Y*3 + 3):
        for j in range(box_X * 3, box_X * 3 + 3):
            if sudoku_board[i][j] == input_num and (i, j) != position:  # sudoku_board[position[0]][position[1]]
                return False

    return True


def solve(sudoku_board):
    empty = find_empty(sudoku_board)

    # Establish Recursion Base Case
    if not empty:
        return True
    else:
        row, col = empty
        for i in range(1,10):
            if valid_input(sudoku_board, i, (row, col)):
                sudoku_board[row][col] = i

                if solve(sudoku_board):
                    return True

                sudoku_board[row][col] = 0

        return False


print_board(board)
solve(board)
print("")
print("")
print("")
print_board(board)





















