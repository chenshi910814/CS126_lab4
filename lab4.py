#lab 4
#Ammon Plerson
#Shi Chen, sc2592@nau.edu

#define a square
def square():
    board = []
    square = ['empty square','full square']
square=[
[1,2,3],
[3,4,5],
[6,8,9],
]

for _ in square: 
    print(_)

#input function
please chose a row number(0-4)
please choose a column number (0-4)
You won with ... moves!

#define the main function 
def main():
    board = [...]

    randomize(board)
    moves = 0 
    while not is_solved(board):
        show(board)
        (row,col) = solicit_row_and_col()
        touch(board, row, col)
        moves += 1
    show(board)
    print(f"You won with {moves} moves!")
