#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#Responsible for GUI and entertaining the user!
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
import pygame

def main():
    screen_width = 720
    screen_height = 720
    grid_width = screen_width/8
    grid_height = screen_height/8

    light_square_col = (230,196,133)
    dark_square_col = (166,102,65)

    chess_screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Chess")
    clock = pygame.time.Clock()

    def draw_chessboard(screen):
        for i in range(0,8):
            for j in range(0,8):
                r = pygame.Rect(i*grid_width, j*grid_height, grid_width, grid_height)
                if (i+j) % 2 == 0:
                    pygame.draw.rect(screen, light_square_col, r)
                else:
                    pygame.draw.rect(screen, dark_square_col, r)


    while (True):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw_chessboard(chess_screen)
        pygame.display.update()
        clock.tick(1)



if __name__ == "__main__":
    main()