import random
import numpy
import game as g

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
options = [[UP, RIGHT, DOWN, LEFT], [RIGHT, DOWN, LEFT, UP], [LEFT, UP, RIGHT, DOWN]]


def game(square_size):
    playable = [0]
    while not sum(playable):
        board_size = get_size()
        pieces_per_player = get_pieces_per_player(board_size)
        types_of_piece = get_types_of_piece(min(pieces_per_player, 7))
        legal_moves = get_moves(types_of_piece, min(board_size)//2)
        starting_board = get_starting_positions(pieces_per_player, types_of_piece, board_size)
        test_game = g.Game([board_size, legal_moves, square_size, starting_board])
        playable = [0 for _ in range(types_of_piece)]
        for y in range(board_size[1]//2):
            for x in range(board_size[0]):
                for y2 in range(board_size[1]):
                    for x2 in range(board_size[0]):
                        if test_game.board.place([x, y], [x2, y2], 0):
                            playable[int(test_game.board.get_piece_at(x2, y2)[1])] = 1




def get_moves(num_of_pieces, max_move_length):
    all_moves = []
    for i in range(num_of_pieces):
        not_right = True
        while not_right:
            not_right = 0
            directional_move = [random.randrange(0, 4) for _ in range(max_move_length)]
            raw_move = []
            for j in range(4):
                x, y = 0, 0
                for part in directional_move:
                    if part:
                        action = options[part - 1][j]
                        if action == UP:
                            y -= 1
                        elif action == RIGHT:
                            x += 1
                        elif action == LEFT:
                            x -= 1
                        elif action == DOWN:
                            y += 1
                if x != 0 and y != 0:
                    raw_move.append([x, y])
                else:
                    not_right = 1
            if not not_right:
                all_moves.append(raw_move)
    return all_moves


def get_size():
    return [random.randrange(3, 21), random.randrange(3, 21)]


def get_pieces_per_player(board_size):
    return random.randrange(1, (1+board_size[1])//2)*board_size[0]


def get_types_of_piece(max_pieces):
    return random.randrange(1, max_pieces+1)


def get_starting_positions(total_pieces, num_of_types, boardsize):
    pieces = [[] for _ in range(1+((total_pieces-1)//boardsize[0]))]
    for i in range(total_pieces):
        pieces[i//boardsize[0]].append(random.randrange(num_of_types))
    board = numpy.zeros([boardsize[1], boardsize[0], 2])
    for y, row1 in enumerate(pieces):
        for x, piece in enumerate(row1):
            board[y][x] = [1, piece]
    for y, row1 in enumerate(pieces):
        for x, piece in enumerate(row1):
            board[-(y+1)][-(x+1)] = [2, piece]

    return board
