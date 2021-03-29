ROOK, KNIGHT, BISHOP, QUEEN, KING = 'r', 'n', 'b', 'q', 'k'
SPACE = ' '

def can_rook_move(from_pos, to_pos, board_view):
    if from_pos[0] == to_pos[0]: 
        col = from_pos[0]
        return all(board_view[col + chr(row)] == SPACE for row in range(ord(from_pos[1]) + 1, ord(to_pos[1])))

    elif from_pos[1] == to_pos[1]:
        row = from_pos[1]
        return all(board_view[chr(col) + row] == SPACE for col in range(ord(from_pos[0]) + 1, ord(to_pos[0])))

    else:
        return False

def can_bishop_move(from_pos, to_pos, board_view):
    if abs(ord(from_pos[0]) - ord(to_pos[0])) == abs(ord(from_pos[1]) - ord(to_pos[1])): 
        change_col_by = 1 if ord(from_pos[0]) < ord(to_pos[0]) else -1
        change_row_by = 1 if ord(from_pos[1]) < ord(to_pos[1]) else -1

        return all(board_view[chr(col) + chr(row)] == SPACE for col, row in 
                zip(range(ord(from_pos[0]) + change_col_by, ord(to_pos[0]), change_col_by), 
                range(ord(from_pos[1]) + change_row_by, ord(to_pos[1]), change_row_by)))

    else:
        return False

def can_knight_move(from_pos, to_pos, board_view):
    return (abs(ord(from_pos[0]) - ord(to_pos[0])) == 2 and abs(ord(from_pos[1]) - ord(to_pos[1])) == 1) \
    or (abs(ord(from_pos[1]) - ord(to_pos[1])) == 2 and abs(ord(from_pos[0]) - ord(to_pos[0])) == 1)

def can_queen_move(from_pos, to_pos, board_view):
    return can_knight_move and can_bishop_move

def can_king_move(from_pos, to_pos, board_view):
    return True

def can_piece_move(piece, from_pos, to_pos, board_view):
    if piece.lower() == ROOK:
        return can_rook_move(from_pos, to_pos, board_view)

    if piece.lower() == KNIGHT:
        return can_knight_move(from_pos, to_pos, board_view)
    
    if piece.lower() == BISHOP:
        return can_bishop_move(from_pos, to_pos, board_view)
    
    if piece.lower() == QUEEN:
        return can_queen_move(from_pos, to_pos, board_view)
    
    if piece.lower() == KING:
        return can_king_move(from_pos, to_pos, board_view)

def pre_compute_move(move):
    piece = move[0]
    from_pos = None
    is_capture = 'x' in move
    to_pos = move[-2:]

    if is_capture:
        if len(move) >= 5:
            from_pos = move[1: -3]
    else:
        if len(move) >= 4:
            from_pos = move[1: -2]

    return piece, from_pos, is_capture, to_pos

def make_piece_move(move, board_view, piece_view):
    piece, from_pos, is_capture, to_pos = pre_compute_move(move)
    if is_capture:
        piece_to_be_removed = board_view[to_pos]
        piece_view[piece_to_be_removed].remove(to_pos)
        board_view[to_pos] = SPACE

    if from_pos != None:
        if len(from_pos) == 1:
            from_pos = [pos for pos in piece_view[piece] if from_pos in pos][0] 
    else:
        if len(piece_view[piece]) == 1:
            from_pos = piece_view[piece][0]
        else:
            from_pos = [pos for pos in piece_view[piece] if can_piece_move(piece, pos, to_pos, board_view)][0]

    board_view[from_pos] = SPACE
    board_view[to_pos] = piece

    piece_view[piece].remove(from_pos)
    piece_view[piece].append(to_pos)

    return board_view, piece_view