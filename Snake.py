import pygame
#Things we need
#initialise pygame
#make the pygame.display and set_mode (size of the screen)
#Set a caption
#get your clock out
#check for the es that have happened (if pygame.QUIT, then outside the loop, we do pygame.quit() (close pygame) and quit() (close application))


def main():
    screen_width = 480
    screen_height = 480
    grid_size = 20
    grid_width = screen_width/grid_size
    grid_height = screen_height/grid_size
    playing = True

    white = (255,255,255)
    black = (0,0,0)
    green = (0,153,0)
    red = (255,0,0)

    up = (0,-1)
    down = (0,1)
    right = (1,0)
    left = (-1,0)

    startingx = screen_width/2
    startingy = screen_height/2
    snake_colour = green

    

    game_screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()

    class Snake:
        def __init__(self):
            self.head_x = startingx
            self.head_y = startingy
            self.colour = snake_colour
            self.position = [(startingx, startingy)]
            self.length = 1
            self.dir = right
            self.prevdir = right

        
        def update_location(self):
            l = self.legnth
            if l > 1:
                for i in range(1,l):
                    self.position[l - i] = self.position[l - i - 1]
                self.position[0] = ((self.position[0][0] + self.dir[0]*grid_width) % screen_width, (self.position[0][1]  + self.dir[1]*grid_height) % screen_height)
            else:
                self.position[0] = ((self.position[0][0] + self.dir[0]*grid_width) % screen_width, (self.position[0][1]  + self.dir[1]*grid_height) % screen_height)
            self.prevdir = self.dir

        def update_dir(self, new_dir):
            if self.length > 1:
                if new_dir != -self.prevdir:
                    self.dir = new_dir
            else:
                self.dir = new_dir    
            


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