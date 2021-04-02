SPACE = ' '
WHITE_CASTLING_ROW, BLACK_CASTLING_ROW = ['1', '1'], ['8', '8']
KING_SIDE_CASTLING_COLS, QUEEN_SIDE_CASTLING_COLS = ['g', 'f'], ['c', 'd']

def is_king_side_castling(move):
    return len(move) == len(move) == 2

def get_curr_pos(move):
    k_row, r_row = WHITE_CASTLING_ROW if move[0].isupper() else BLACK_CASTLING_ROW
    
    k_col = 'e'
    r_col = 'h' if is_king_side_castling(move) else 'a'

    return k_col + k_row, r_col + r_row

def get_new_pos(move):
    k_row, r_row = WHITE_CASTLING_ROW if move[0].isupper() else BLACK_CASTLING_ROW
    k_col, r_col = KING_SIDE_CASTLING_COLS if is_king_side_castling(move) else QUEEN_SIDE_CASTLING_COLS

    return k_col + k_row, r_col + r_row

def do_castling(move, board_view, piece_view):
    k_curr_pos, r_curr_pos = get_curr_pos(move)
    k_new_pos, r_new_pos = get_new_pos(move)

    king = board_view[k_curr_pos]
    rook = board_view[r_curr_pos]

    piece_view[king].remove(k_curr_pos)
    piece_view[king].append(k_new_pos)

    piece_view[rook].remove(r_curr_pos)
    piece_view[rook].append(r_new_pos)    

    board_view[k_curr_pos] = SPACE
    board_view[r_curr_pos] = SPACE

    board_view[k_new_pos] = king
    board_view[r_new_pos] = rook

    return board_view, piece_view