def is_valid_chess_board(board):
    # if white or black king are in board
    if "bking" not in board.values() or "wking" not in board.values():
        return False

    # check if there is more than 16 piece for each player
    black_pieces = 0
    white_pieces = 0
    for color in board.values():
        if color[0] == "b":
            black_pieces += 1
        elif color[0] == "w":
            white_pieces += 1
    if black_pieces > 16 or white_pieces > 16:
        return False

    if sum(i == "bpawn" for i in board.values()) > 8 or sum(i == "wpawn" for i in board.values()) > 8:
        return False
    
    # check for a valid location 
    valid_columns = ["a", "b", "c", "d", "e", "f", "g", "h"]
    valid_rows = ["1", "2", "3", "4", "5", "6", "7", "8"]

    for position in board.keys():
        column = position[1]  
        row = position[0]     
        if column not in valid_columns or row not in valid_rows:
            return False
    
    # check if pieces names start with b or w
    for pieces in board.values():
        if pieces[0] != 'b' and pieces[0] != 'w':
            return False
    
    # check if pieces have correct names
    piece_names = ["pawn", "knight", "bishop", "rook", "queen", "king"]
    for names in board.values():
        if names[1:] not in piece_names:
            return False
    
    return True

if __name__ == "__main__":
    print(is_valid_chess_board({"1h": "bking", "6c": "wqueen", "2g": "bbishop", "5h": "bqueen", "3e": "wking"}))  # True
    print(is_valid_chess_board({"1a": "bpawn", "2a": "wking"}))  # False
    print(is_valid_chess_board({"1a": "wking", "2a": "wking", "3c": "bbishop"}))  # False
    print(is_valid_chess_board({"1a": "bking", "9z": "wking"}))  # False