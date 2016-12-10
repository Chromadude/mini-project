from board import Board

"""
Options

0: board size
1: legal moves for each piece
"""


class Game:
    def __init__(self, options):
        self.board = Board(options[0], options[1])
