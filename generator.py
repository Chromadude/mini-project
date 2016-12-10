import random

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
options = [[UP, RIGHT, DOWN, LEFT], [RIGHT, DOWN, LEFT, UP], [LEFT, UP, RIGHT, DOWN]]


def generate_moves(num_of_pieces, max_move_length):
    moves = []
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
                moves.append(raw_move)
    return moves


def generate_size():
    return [random.randrange(3, 21), random.randrange(3, 21)]
