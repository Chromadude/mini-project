import game
import generator
import pygame

size = generator.size()
pieces_per_player = generator.pieces_per_player(size)
types_of_piece = generator.types_of_piece(pieces_per_player)
legal_moves = generator.moves(types_of_piece, 4)
g = game.Game([size, legal_moves, 48])
g.board.set_piece_at(0, 0, [1, 0])
pygame.init()
surface = pygame.display.set_mode((g.board.screenwidth, g.board.screenheight))
g.start(surface)
