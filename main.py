"""Parse moves to get the final state of the board."""

import sys

from os import path

from pre_process_pgn_file import pgn_to_moves
from piece import make_piece_move
from pawn import make_pawn_move
from castling import do_castling
from print_board import print_board

SPACE, END = " ", "end"
ROWS, COLS = "12345678", "abcdefgh"
START = "RNBQKBNRPPPPPPPP" + SPACE * 8 * 4 + "pppppppprnbqkbnr"
PAWN, CASTLING = "p", "o"


def setup():
    sqrs = [x + y for y in ROWS for x in COLS]
    board_view = dict(zip(sqrs, START))

    piece_view = {pc: [] for pc in "rnbqkpRNBQKP"}
    for pos in board_view:
        piece = board_view[pos]

        if piece != SPACE:
            piece_view[piece].append(pos)

    return board_view, piece_view


def make_move(move, board_view, piece_view):
    if move == END:
        return board_view, piece_view
    if move[0].lower() == PAWN:
        make_pawn_move(move, board_view, piece_view)
    elif move[0].lower() == CASTLING:
        do_castling(move, board_view, piece_view)
    else:
        make_piece_move(move, board_view, piece_view)
    return board_view, piece_view


def parse(pgn_file):
    if not path.exists(pgn_file):
        print("pgn file path does not exist.")
        sys.exit(1)

    board_view, piece_view = setup()
    moves = pgn_to_moves(pgn_file)

    for w_move, b_move in moves:
        board_view, piece_view = make_move(w_move, board_view, piece_view)
        board_view, piece_view = make_move(b_move, board_view, piece_view)

    print_board(board_view)


if __name__ == "__main__":
    parse(sys.argv[1])
