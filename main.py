import game
import generator
import pygame

size = generator.size()
pieces_per_player = generator.pieces_per_player(size)
types_of_piece = generator.types_of_piece(min(pieces_per_player, 7))
legal_moves = generator.moves(types_of_piece, 4)
starting_board = generator.starting_positions(pieces_per_player, types_of_piece, size)
g = game.Game([size, legal_moves, 48, starting_board])
pygame.init()
surface = pygame.display.set_mode((g.board.screenwidth, g.board.screenheight))
g.start(surface)
