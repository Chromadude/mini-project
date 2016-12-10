import random

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
options = [[UP, RIGHT, DOWN, LEFT], [RIGHT, DOWN, LEFT, UP], [LEFT, UP, RIGHT, DOWN]]


def generate_moves(num_of_pieces, max_move_length):
    moves = []
    for i in range(num_of_pieces):
        directional_move = [random.randrange(0, 4) for _ in range(max_move_length)]
        raw_move = []
        for j in range(4):
            x, y = 0, 0
            for part in directional_move:
                if part:
                    action = options[part-1][j]
                    if action == UP:
                        y -= 1
                    elif action == RIGHT:
                        x += 1
                    elif action == LEFT:
                        x -= 1
                    elif action == DOWN:
                        y += 1
            raw_move.append([x, y])
        moves.append(raw_move)
    return moves


def generate_size():
    return [random.randrange(3, 21), random.randrange(3, 21)]
