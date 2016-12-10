import random
import numpy

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
options = [[UP, RIGHT, DOWN, LEFT], [RIGHT, DOWN, LEFT, UP], [LEFT, UP, RIGHT, DOWN]]


def moves(num_of_pieces, max_move_length):
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


def size():
    return [random.randrange(3, 21), random.randrange(3, 21)]


def pieces_per_player(board_size):
    return random.randrange(1, (1+board_size[1])//2)*board_size[0]


def types_of_piece(max_pieces):
    return random.randrange(1, max_pieces+1)


def starting_positions(total_pieces, num_of_types, boardsize):
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
