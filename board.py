import numpy as np
import pygame


class Board:
    def __init__(self, size, legal_moves, squaresize):
        # grid of: (owner, type)
        # owner is 0: empty, 1: player 1 etc
        self.rows = np.zeros([size[1], size[0], 2])
        self.legal_moves = legal_moves
        self.squaresize = squaresize
        self.screenwidth = squaresize*size[0]
        self.screenheight = squaresize*size[1]

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
                pygame.draw.line(surf, (0, 0, 0), (x* self.squaresize, 0), (x * self.squaresize, self.screenheight))
                pygame.draw.line(surf, (0, 0, 0), (0, y * self.squaresize), (self.screenwidth, y * self.squaresize))
                if value[0]:
                    surf.blit(images[int(value[1] + (value[0] - 1) * 7)], (x * self.squaresize, y * self.squaresize))


import generator

# pygame.init()
# surface = pygame.display.set_mode((width * SQUARESIZE, height * SQUARESIZE))
# b = Board([width, height])
# images = load_shapes()
# b.draw(surface, images)
