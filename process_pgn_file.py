import re

SPACE = " "

def pgn_to_moves(pgn_file):
    raw_pgn = SPACE.join([line.strip() for line in pgn_file])

    comments_marked = raw_pgn.replace("{", "<").replace("}", ">")
    STRC = re.compile("<[^>]*>")
    comments_removed = STRC.sub(" ", comments_marked)

    str_marked = comments_removed.replace("[", "<").replace("]", ">")
    str_removed = STRC.sub(" ", str_marked)

    print(str_removed)

pgn_to_moves(open())