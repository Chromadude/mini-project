import game
import generator
import pygame

playable = [0]
while not sum(playable):
    size = generator.size()
    pieces_per_player = generator.pieces_per_player(size)
    types_of_piece = generator.types_of_piece(min(pieces_per_player, 7))
    legal_moves = generator.moves(types_of_piece, 4)
    starting_board = generator.starting_positions(pieces_per_player, types_of_piece, size)
    test_game = game.Game([size, legal_moves, 48, starting_board])
    playable = [0 for _ in range(types_of_piece)]
    for y in range(size[1]//2):
        for x in range(size[0]):
            for y2 in range(size[1]):
                for x2 in range(size[0]):
                    if test_game.board.place([x, y], [x2, y2], 0):
                        playable[int(test_game.board.get_piece_at(x2, y2)[1])] = 1
g = game.Game([size, legal_moves, 48, starting_board])
pygame.init()
surface = pygame.display.set_mode((g.board.screenwidth, g.board.screenheight))
g.start(surface)
