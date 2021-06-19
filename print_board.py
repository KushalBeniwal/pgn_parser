'''Print board state.

P.S. ignore this file for good coding practices, 
was done coding and had no energy to do anymore changes.

Update: cleaning up but still no energy to do any changes here.'''

def print_board(board_view):
    print("  a b c d e f g h")
    for pos in board_view:
        if pos[0] == "a":
            print(pos[1], end=" ")
        print(board_view[pos], end=" ")
        if pos[0] == "h":
            print(pos[1])
    print("  a b c d e f g h")
