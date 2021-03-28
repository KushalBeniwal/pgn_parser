import sys
import process_pgn_file

from os import path

SPACE = " "
ROWS, COLS = "12345678", "abcdefgh"
START = "rnbqkbnrpppppppp" + SPACE * 8 * 4 + "RNBQKBNRPPPPPPPP"

def setup():
    sqrs = [y+x for y in COLS for x in ROWS]
    board_view = dict(zip(sqrs, START))

    piece_view = {pc: [] for pc in "rnbqkpRNBQKP"}
    for pos in board_view:
        piece = board_view[pos]

        if piece != SPACE:
            piece_view[piece].append(pos)

    return board_view, piece_view

def parse(pgn_file):
    if not path.exists(pgn_file):
        print("pgn file path doesn't exist.")
        sys.exit(1)

    board_view, piece_view = setup()

if __name__=="__main__":
    parse(sys.argv[1])