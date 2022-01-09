# %%

from typing import Sized
import pygame
import Piece
import Board as Bd
# set up window
screen = pygame.display.set_mode([800, 800])
background_colour = (44, 44, 84)


class Square():
    def __init__(self, x_pos, y_pos, size=100, colour=background_colour):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.colour = background_colour
        self.size = size

    def square_drawer(self):
        pygame.draw.rect(screen, self.colour, pygame.Rect(
            self.x_pos, self.y_pos, self.size, self.size))


rectangles = []
for i in range(0, 8):
    for j in range(0, 8, 2):
        if i % 2 == 1:
            rectangles.append(Square(i*100, j*100))
        if i % 2 == 0:
            rectangles.append(Square(i*100, (j+1)*100))


chess_board = Bd.Board()
chess_board.print_board()


pygame.init()


# run until user quits
running = True
while running:
    # Quit case
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Creating the background.
    screen.fill((225, 218, 189))
    screen.lock()
    for rectangle in rectangles:
        rectangle.square_drawer()

    screen.unlock()
    pygame.display.update()
pygame.quit()

# %%
