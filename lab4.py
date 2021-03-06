# lab 4
# Ammon Plerson
# Shi Chen, sc2592@nau.edu
import random
# the squares used to represent lights
WHITE_SQUARE = "\N{WHITE SQUARE}"
BLACK_SQUARE = "\N{BLACK SQUARE}"

# i is the list; j is the element in the list
# set board to lights out and then press 10 random squares to make it solvable


def randomize(board):
    for i in range(5):
        for j in range(5):
            board[i][j] = True
        for i in range(10):
            touch(board, random.randrange(0, 5), random.randrange(0, 5))


def is_solved(board):
    for row in board:
        for square in row:
            if not square:
                return False
    return True

# user chooses row and column for game


def solicit_row_and_col():
    row = int(input("Please choose a row number (0-4): "))
    column = int(input("Please choose a column number (0-4):"))
    return row, column


def show(board):
    for row in board:
        row_string = " ".join(
            [WHITE_SQUARE if square else BLACK_SQUARE for square in row]
        )
        print(row_string)

# peramiters


def touch(board, row, col):
    board[row][col] = not board[row][col]
    if row > 0:
        board[row - 1][col] = not board[row - 1][col]

    if col > 0:
        board[row][col - 1] = not board[row][col - 1]

    if row < 4:
        board[row + 1][col] = not board[row + 1][col]

    if col < 4:
        board[row][col + 1] = not board[row][col + 1]


# define the main function and show winning statment
def main():
    board = [[True] * 5 for i in range(5)]

    randomize(board)
    moves = 0
    while not is_solved(board):
        show(board)
        (row, col) = solicit_row_and_col()
        touch(board, row, col)
        moves += 1
    show(board)
    print(f"You won with {moves} moves!")


if __name__ == "__main__":
    main()
