import numpy as np
import pygame

SQUARESIZE = 48
width, height = 19, 19
SCREENWIDTH = SQUARESIZE * width
SCREENHEIGHT = SQUARESIZE * height

shapes_designs = [
    [0, [[[0, 0], [1, 1]], [[1, 0], [0, 1]]]],
    [0, [[[0.5, 0], [1, 0.75], [0, 0.75], [0.5, 0]]]],
    [1, [0.5, 0.5, 0.5]],
    [0, [[[0.5, 0], [0.5, 1]], [[0, 0.5], [1, 0.5]]]],
    [0, [[[0.5, 0], [1, 0.5], [0.5, 1], [0, 0.5], [0.5, 0]]]],
    [0, [[[0.5, 0], [0.5, 1]], [[0, 0.5], [1, 0.5]], [[0, 0], [1, 1]], [[1, 0], [0, 1]]]],
    [0, [[[0.25, 0], [0.25, 1]], [[0.75, 0], [0.75, 1]], [[0, 0.25], [1, 0.25]], [[0, 0.75], [1, 0.75]]]]
]


def load_shapes():
    shapes = [pygame.Surface((SQUARESIZE, SQUARESIZE), pygame.SRCALPHA, 32).convert_alpha() for _ in range(14)]
    for i, shape in enumerate(shapes_designs):
        if shapes_designs[i][0]:
            circle = shapes_designs[i][1]
            pygame.draw.circle(shapes[i], (0, 0, 0), (int(circle[0] * SQUARESIZE), int(circle[1] * SQUARESIZE)),
                               int(circle[2] * SQUARESIZE))
        else:
            for lines in shapes_designs[i][1]:
                pygame.draw.lines(shapes[i], (0, 0, 0), 0,
                                  [[int(d * SQUARESIZE) for d in point] for point in lines], int(SQUARESIZE / 16))
    for i, shape in enumerate(shapes_designs):
        if shapes_designs[i][0]:
            circle = shapes_designs[i][1]
            pygame.draw.circle(shapes[i + 7], (255, 0, 0), (int(circle[0] * SQUARESIZE), int(circle[1] * SQUARESIZE)),
                               int(circle[2] * SQUARESIZE))
        else:
            for lines in shapes_designs[i][1]:
                pygame.draw.lines(shapes[i + 7], (255, 0, 0), 0,
                                  [[int(d * SQUARESIZE) for d in point] for point in lines], int(SQUARESIZE / 16))
    return shapes


class Board:
    def __init__(self, size, legal_moves):
        # grid of: (owner, type)
        # owner is 0: empty, 1: player 1 etc
        self.rows = np.zeros(size + [2])
        self.legal_moves = legal_moves

    def get_piece_at(self, x, y):
        return self.rows[y][x]

    def set_piece_at(self, x, y, new_piece):
        self.rows[y][x] = new_piece

    def place(self, initial_coord, new_coord, player):
        piece = self.get_piece_at(*initial_coord)
        if piece[0] != player+1:
            return 0
        changex, changey = new_coord[0] - initial_coord[0], new_coord[1] - initial_coord[1]
        for move in self.legal_moves[int(piece[1])]:
            if move[0] == changex and move[1] == changey:
                self.set_piece_at(*new_coord, piece)
                self.set_piece_at(*initial_coord, [0, 0])
                return 1
        return 0

    def draw(self, surf, images):
        surf.fill((255, 255, 255))

        for y, row in enumerate(self.rows):
            for x, value in enumerate(row):
                pygame.draw.line(surf, (0, 0, 0), (x * SQUARESIZE, 0), (x * SQUARESIZE, SCREENHEIGHT))
                pygame.draw.line(surf, (0, 0, 0), (0, y * SQUARESIZE), (SCREENWIDTH, y * SQUARESIZE))
                if value[0]:
                    surf.blit(images[int(value[1] + (value[0] - 1) * 7)], (x * SQUARESIZE, y * SQUARESIZE))
        pygame.display.flip()


import generator

# pygame.init()
# surface = pygame.display.set_mode((width * SQUARESIZE, height * SQUARESIZE))
# b = Board([width, height])
# images = load_shapes()
# b.draw(surface, images)
