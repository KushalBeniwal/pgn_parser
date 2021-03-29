SPACE = ' '
EN_PASSANT_ROW_TO = {'4': '3', '5': '6'}
PAWN_TO_REMOVE = {'p': 'P', 'P': 'p'}
REGULAR_DOUBLE_MOVE_TO = {'p': '5', 'P': '4'}
REGULAR_DOUBLE_MOVE_FROM = {'p': '7', 'P': '2'}

def promote(piece, move_to, promote_to, board_view, piece_view):
    board_view[move_to] = promote_to

    piece_view[piece].remove(move_to)
    piece_view[promote_to].append(move_to)

    return board_view, piece_view

def make_normal_move(piece, move_to, board_view, piece_view):
    if move_to[-1] == REGULAR_DOUBLE_MOVE_TO[piece] and board_view[move_to[0] + REGULAR_DOUBLE_MOVE_FROM[piece]] == piece:
        move_from = move_to[0] + REGULAR_DOUBLE_MOVE_FROM[piece]
    else:
        move_from = move_to[0] + chr(ord(move_to[-1]) + (-1 if piece.isupper() else 1))

    board_view[move_from] = SPACE
    board_view[move_to] = piece

    piece_view[piece].remove(move_from)
    piece_view[piece].append(move_to)

    return board_view, piece_view

def make_capture(piece, move_to, move_from, board_view, piece_view):
    if move_from == None:
        if chr(ord(move_to[0]) + 1) + chr(ord(move_to[1]) + (1 if piece.isupper() else -1)) in piece_view[piece]:
            move_from = chr(ord(move_to[0]) + 1) + chr(ord(move_to[1]) + (1 if piece.isupper() else -1))
        else:
            move_from = chr(ord(move_to[0]) - 1) + chr(ord(move_to[1]) + (1 if piece.isupper() else -1))
    else:
        move_from += chr(ord(move_to[1]) + (-1 if piece.isupper() else 1))

    piece_to_remove = board_view[move_to]
    piece_view[piece_to_remove].remove(move_to)
    board_view[move_to] = SPACE

    board_view[move_from] = SPACE
    board_view[move_to] = piece

    piece_view[piece].remove(move_from)
    piece_view[piece].append(move_to)

    return board_view, piece_view
    

def make_en_passant(piece, move_to, move_from, board_view, piece_view):
    if move_from == None:
        if chr(ord(move_to[0]) + 1) + EN_PASSANT_ROW_TO[move_to[-1]] in piece_view[piece]:
            move_from = chr(ord(move_to[0]) + 1) + EN_PASSANT_ROW_TO[move_to[-1]] 
        else:
            move_from = chr(ord(move_to[0]) - 1) + EN_PASSANT_ROW_TO[move_to[-1]]
    else:
        move_from += EN_PASSANT_ROW_TO[move_to[-1]]

    index_of_pawn_to_remove = move_to[0] + EN_PASSANT_ROW_TO[move_to[-1]]

    piece_view[PAWN_TO_REMOVE[piece]].remove(index_of_pawn_to_remove)
    board_view[index_of_pawn_to_remove] = SPACE

    board_view[move_from] = SPACE
    board_view[move_to] = piece

    piece_view[piece].remove(move_from)
    piece_view[piece].append(move_to)

    return board_view, piece_view

def is_capture(move):
    return 'x' in move

def is_promotion(move):
    return not move[-1].isnumeric()

def is_enpassant(move, move_to, board_view):
    return board_view[move_to] == SPACE and is_capture(move)

def make_pawn_move(move, board_view, piece_view):
    piece = move[0]
    move_to = move[-3: -1] if is_promotion(move) else move[-2:]
    if is_capture(move):
        move_from = move[1] if move[1] != 'x' else None

    if is_enpassant(move, move_to, board_view):
        board_view, piece_view = make_en_passant(piece, move_to, move_from, board_view, piece_view)

    elif is_capture(move):
        board_view, piece_view = make_capture(piece, move_to, move_from, board_view, piece_view)

    else:
        board_view, piece_view = make_normal_move(piece, move_to, board_view, piece_view)

    if is_promotion(move):
        promote_to = move[-1]
        board_view, piece_view = promote(piece, move_to, promote_to, board_view, piece_view)
    
    return board_view, piece_view