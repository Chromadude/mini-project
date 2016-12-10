import game
from generator import generate_moves, generate_size
import pygame

g = game.Game([generate_size(), generate_moves(4, 4), 48])
print(g.legalmoves)
g.board.set_piece_at(0, 0, [1, 0])
pygame.init()
surface = pygame.display.set_mode((g.board.screenwidth, g.board.screenheight))
g.start(surface)
