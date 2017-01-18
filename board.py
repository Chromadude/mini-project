import numpy as np
import pygame


class Board:
    def __init__(self, size, legal_moves, squaresize, starting_board):
        # grid of: (owner, type)
        # owner is 0: empty, 1: player 1 etc
        self.rows = np.array(starting_board)
        self.legal_moves = legal_moves
        self.squaresize = squaresize
        self.screenwidth = squaresize * size[0]
        self.screenheight = squaresize * size[1]
        self.starting_board = starting_board

    def reset(self):
        self.rows = np.array(self.starting_board)

    def get_piece_at(self, x, y):
        return self.rows[y][x]

    def set_piece_at(self, x, y, new_piece):
        self.rows[y][x] = new_piece

    def place(self, initial_coord, new_coord, player):
        piece = self.get_piece_at(*initial_coord)
        if piece[0] != player + 1:
            return 0
        changex, changey = new_coord[0] - initial_coord[0], new_coord[1] - initial_coord[1]
        for move in self.legal_moves[int(piece[1])]:
            if move[0] == changex and move[1] == changey:
                if self.get_piece_at(*new_coord)[0] == player + 1:
                    return 0
                else:
                    self.set_piece_at(*new_coord, piece)
                    self.set_piece_at(*initial_coord, [0, 0])
                    return 1
        return 0

    def draw(self, surf, images):
        surf.fill((255, 255, 255))

        for y, row in enumerate(self.rows):
            for x, value in enumerate(row):
                pygame.draw.line(surf, (0, 0, 0), (x * self.squaresize, 0), (x * self.squaresize, self.screenheight))
                pygame.draw.line(surf, (0, 0, 0), (0, y * self.squaresize), (self.screenwidth, y * self.squaresize))
                if value[0]:
                    surf.blit(images[int(value[1] + (value[0] - 1) * 7)], (x * self.squaresize, y * self.squaresize))

    def ended(self):
        dead = [1, 1]
        for row in self.rows:
            for piece in row:
                if piece[0] == 1:
                    dead[0] = 0
                elif piece[0] == 2:
                    dead[1] = 0
        return sum(dead) == 1

    def get_possible_moves(self, player):
        moves = []
        for y, row in enumerate(self.rows):
            for x, square in enumerate(row):
                for i in range(4):
                    move = [[x, y],
                            [x + self.legal_moves[int(square[1])][i][0], y + self.legal_moves[int(square[1])][i][1]]]
                    if 0 <= move[1][0] < len(row) and 0 <= move[1][1] < len(self.rows) and \
                            self.get_piece_at(*move[1])[0] != player+1:
                        moves.append(move)
        return moves

