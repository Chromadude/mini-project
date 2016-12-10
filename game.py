import board
import pygame

"""
Options

0: board size
1: legal moves for each piece
2: squaresize
"""


class Game:
    def __init__(self, options):
        self.board = board.Board(*options)
        self.size = options[0]
        self.legalmoves = options[1]
        self.squaresize = options[2]
        self.player = 0
        self.held = 0

    def start(self, surface):
        images = load_shapes(self.squaresize)
        playing = 1
        while playing:
            self.board.draw(surface, images)
            if self.held:
                x, y = pygame.mouse.get_pos()
                x = x // self.squaresize
                y = y // self.squaresize
                surface.blit(images[int(self.held[0][1] + (self.held[0][0] - 1) * 7)],
                             (x * self.squaresize, y * self.squaresize))
            pygame.display.flip()
            events = []
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return
                else:
                    events.append(event)
            self.user_handle(events)
            if self.board.ended():
                return int(not self.player)

    def user_handle(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = pygame.mouse.get_pos()
                    x = x // self.squaresize
                    y = y // self.squaresize
                    piece = self.board.get_piece_at(x, y)
                    if piece[0] == self.player + 1:
                        self.held = piece, (x, y)
            if event.type == pygame.MOUSEBUTTONUP and self.held and event.button == 1:
                x, y = pygame.mouse.get_pos()
                x = x // self.squaresize
                y = y // self.squaresize
                if 0 <= x < self.size[0] and 0 <= y < self.size[1]:
                    if self.board.place(self.held[1], (x, y), self.player):
                        self.player = not self.player
                self.held = 0


shapes_designs = [
    [0, [[[0, 0], [1, 1]], [[1, 0], [0, 1]]]],
    [0, [[[0.5, 0], [1, 0.75], [0, 0.75], [0.5, 0]]]],
    [1, [0.5, 0.5, 0.5]],
    [0, [[[0.5, 0], [0.5, 1]], [[0, 0.5], [1, 0.5]]]],
    [0, [[[0.5, 0], [1, 0.5], [0.5, 1], [0, 0.5], [0.5, 0]]]],
    [0, [[[0.5, 0], [0.5, 1]], [[0, 0.5], [1, 0.5]], [[0, 0], [1, 1]], [[1, 0], [0, 1]]]],
    [0, [[[0.25, 0], [0.25, 1]], [[0.75, 0], [0.75, 1]], [[0, 0.25], [1, 0.25]], [[0, 0.75], [1, 0.75]]]]
]


def load_shapes(squaresize):
    shapes = [pygame.Surface((squaresize, squaresize), pygame.SRCALPHA, 32).convert_alpha() for _ in range(14)]
    for i, shape in enumerate(shapes_designs):
        if shapes_designs[i][0]:
            circle = shapes_designs[i][1]
            pygame.draw.circle(shapes[i], (0, 0, 0), (int(circle[0] * squaresize), int(circle[1] * squaresize)),
                               int(circle[2] * squaresize))
        else:
            for lines in shapes_designs[i][1]:
                pygame.draw.lines(shapes[i], (0, 0, 0), 0,
                                  [[int(d * squaresize) for d in point] for point in lines], int(squaresize / 16))
    for i, shape in enumerate(shapes_designs):
        if shapes_designs[i][0]:
            circle = shapes_designs[i][1]
            pygame.draw.circle(shapes[i + 7], (255, 0, 0), (int(circle[0] * squaresize), int(circle[1] * squaresize)),
                               int(circle[2] * squaresize))
        else:
            for lines in shapes_designs[i][1]:
                pygame.draw.lines(shapes[i + 7], (255, 0, 0), 0,
                                  [[int(d * squaresize) for d in point] for point in lines], int(squaresize / 16))
    return shapes
