from typing import TYPE_CHECKING
import pygame
import random
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
    fruit_colour = red

    

    game_screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()

    class Fruit:
        def __init__(self, x, y):
            self.position = (x,y)
            self.colour = fruit_colour

        def reposition(self, x, y):
            self.position = (x,y)

    class Snake:
        def __init__(self):
            self.head_x = startingx
            self.head_y = startingy
            self.colour = snake_colour
            self.position = [(startingx, startingy)]
            self.length = 1
            self.dir = right
            self.prevdir = right
            self.intersect = False
            self.eating = False
            self.grow = False

        def update_location(self):
            l = self.length
            if l > 1:
                for i in range(1,l):
                    self.position[l - i] = self.position[l - i - 1]
                self.position[0] = ((self.position[0][0] + self.dir[0]*grid_width) % screen_width, (self.position[0][1]  + self.dir[1]*grid_height) % screen_height)
            else:
                self.position[0] = ((self.position[0][0] + self.dir[0]*grid_width) % screen_width, (self.position[0][1]  + self.dir[1]*grid_height) % screen_height)
            self.prevdir = self.dir

        def update_dir(self, new_dir):
            opposite_new_dir = (-new_dir[0], -new_dir[1])
            if self.length > 1:
                
                if opposite_new_dir != self.prevdir:
                    self.dir = new_dir
            else:
                self.dir = new_dir
            
        def check_intersect(self):
            if self.length > 2:
                for i in range(1,self.length):
                    if self.position[0] == self.position[i]:
                        self.intersect = True

        def check_eaten_fruit(self, fruitx, fruity):
            if ((self.position[0][0] + self.dir[0]*grid_width) % screen_width, (self.position[0][1]  + self.dir[1]*grid_height) % screen_height) == (fruitx, fruity):
                self.eating = True

        def growing_update_location(self):
            self.length += 1
            self.position = self.position + [self.position[(self.length - 2)]]
            self.position[1:(self.length - 1)] = self.position[0:(self.length - 2)]
            self.position[0] = ((self.position[0][0] + self.dir[0]*grid_width) % screen_width, (self.position[0][1]  + self.dir[1]*grid_height) % screen_height)
            self.prevdir = self.dir

    snake = Snake()
    fruit = Fruit(random.randint(0, grid_size - 1)*grid_width, random.randint(0, grid_size - 1)*grid_height)

    def draw_gamescreen(game_screen):
        game_screen.fill(black)
        r = pygame.Rect(fruit.position[0], fruit.position[1], grid_width, grid_height)
        pygame.draw.rect(game_screen, fruit.colour, r)
        for i in range(0, snake.length):
            r = pygame.Rect(snake.position[i][0], snake.position[i][1], grid_width, grid_height)
            pygame.draw.rect(game_screen, snake.colour, r)


    while playing:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()

            if e.type == pygame.KEYDOWN:
                match e.key:
                    case pygame.K_LEFT:
                        snake.update_dir(left)
                    case pygame.K_RIGHT:
                        snake.update_dir(right)
                    case pygame.K_UP:
                        snake.update_dir(up)
                    case pygame.K_DOWN:
                        snake.update_dir(down)
        
        snake.check_eaten_fruit(fruit.position[0], fruit.position[1])
        if snake.eating == True:
            fruit.reposition(random.randint(0, grid_size - 1)*grid_width, random.randint(0, grid_size - 1)*grid_height)
            snake.update_location()
            snake.eating = False
            snake.grow = True
        elif snake.grow == True:
            snake.growing_update_location()
            snake.grow = False
        else:
            snake.update_location()

        draw_gamescreen(game_screen)
        pygame.display.update()
        snake.check_intersect()
        if snake.intersect == True:
            snake = Snake()
        clock.tick(10)


if __name__ == "__main__":
    main()

pygame.quit()
quit()