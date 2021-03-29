SPACE = ' '

def is_king_side_castling(move):
    return len(move) == len(move) == 2

def get_curr_pos(move):
    if move[0].isupper():
        k_row, r_row = '1', '1' 
    else:
        k_row, r_row = '8', '8'
    
    k_col = 'e'

    if is_king_side_castling(move):
        r_col = 'h'
    else:
        r_col = 'a'

    return k_col + k_row, r_col + r_row

def get_new_pos(move):
    if move[0].isupper():
        k_row, r_row = '1', '1' 
    else:
        k_row, r_row = '8', '8'

    if is_king_side_castling(move):
        k_col, r_col = 'g', 'f'
    else:
        k_col, r_col = 'c', 'd'

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