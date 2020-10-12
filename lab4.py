#lights out
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
