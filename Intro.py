import pygame
#Things we need
#initialise pygame
#make the pygame.display and set_mode (size of the screen)
#Set a caption
#get your clock out
#check for the es that have happened (if pygame.QUIT, then outside the loop, we do pygame.quit() (close pygame) and quit() (close application))


def main():

    class Ball:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.speed = (0,0)
            self.colour = black

        def change_speed(self, speed):
            self.speed = speed

        def change_location(self):
            self.x = self.x + self.speed[0]
            self.y = self.y + self.speed[1]

    screen_width = 480
    screen_height = 480
    grid_size = 20
    grid_width = screen_width/grid_size
    grid_height = screen_height/grid_size
    playing = True


    white = (255,255,255)
    black = (0,0,0)
    game_screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("A ball.")
    clock = pygame.time.Clock()

    ball = Ball(20,20)

    def draw_gamescreen(game_screen):
        pygame.fill(game_screen, white)
        r = pygame.Rect(ball.x, ball.y, 20, 20)
        game_screen.draw.rect(r, ball.colour)


    while playing:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()

            if e.type == pygame.KEYDOWN:
                match e.key:
                    case pygame.K_LEFT:
                        ball.change_speed((-20, 0))
                    case pygame.K_RIGHT:
                        ball.change_speed((20, 0))
                    case pygame.K_UP:
                        ball.change_speed((0, -20))
                    case pygame.K_DOWN:
                        ball.change_speed((0, 20))

            if e.type == pygame.KEYUP:
                if e.key == pygame.K_LEFT or e.key == pygame.K_RIGHT or e.key == pygame.K_UP or e.key == pygame.K_DOWN:
                    ball.change_speed((0,0))
        
        ball.change_location()
        game_screen.fill(white)
        r = pygame.Rect(ball.x, ball.y, 20, 20)
        pygame.draw.rect(game_screen, ball.colour, r)
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()

pygame.quit()
quit()