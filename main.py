import game
import pygame
import generator

SQUARESIZE = 32
size, legal_moves, starting_board = generator.game(SQUARESIZE)
g = game.Game([size, legal_moves, SQUARESIZE, starting_board])
pygame.init()
surface = pygame.display.set_mode((g.board.screenwidth, g.board.screenheight))
playing = 1
while playing:
    winner, playing = g.start(surface, "player", "player")
    print(winner)
