'''Pre-process the pgn_file to return (clean)moves only.'''

import re

SPACE = ' '
COLS = 'abcdefgh'
END = ' end'
WHITE_PAWN, BLACK_PAWN = 'P', 'p'

def clean(move):
    return ''.join(filter(str.isalnum, move))

def pre_process_a_move(raw_move):
    w_move, b_move = raw_move.strip().split()

    if w_move[0] in COLS:
        w_move = WHITE_PAWN + w_move

    if b_move[0] in COLS:
        b_move = BLACK_PAWN + b_move
    else:
        b_move = b_move.lower()

    return clean(w_move), clean(b_move)

def pre_process_last_move(last_move):
    if SPACE not in last_move:
        if last_move[0] in COLS:
            last_move = WHITE_PAWN + last_move 
        return (clean(last_move) + END).split()
    else:
        return pre_process_a_move(last_move)

def pgn_to_moves(pgn_file):
    raw_pgn = SPACE.join([line.strip() for line in open(pgn_file)])

    comments_marked = raw_pgn.replace('{', '<').replace('}', '>')
    strc = re.compile('<[^>]*>')
    comments_removed = strc.sub(' ', comments_marked)

    str_marked = comments_removed.replace('[', '<').replace(']', '>')
    str_removed = strc.sub(' ', str_marked)

    move_num = re.compile('[1-9][0-9]* *\.')
    just_moves = [_.strip() for _ in move_num.split(str_removed)]

    last_move = just_moves[-1]
    result = re.compile('( *1 *- *0| *0 *- *1| *1/2 *- *1/2)')
    last_move = result.sub('', last_move)

    return [pre_process_a_move(_) for _ in just_moves[1:-1]] + [pre_process_last_move(last_move)]