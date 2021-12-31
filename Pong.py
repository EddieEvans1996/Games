import pygame
import random
import math

def main():
    screen_width = 960
    screen_height = 480
    paddle_height = 40
    paddle_width = 10
    ball_size = 10
    initial_player_speed = 1
    initial_ball_speed = 1
    multiplyer = 5
    black = (0,0,0)
    white = (255,255,255)

    pygame.init()
    game_screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Pong")
    clock = pygame.time.Clock()
    
    class Player():
        def __init__(self, x):
            self.speed = 0
            self.xloc = x
            self.yloc = (screen_height- paddle_height)/2
            self.score = 0

        def change_speed(self, speed):
            self.speed = speed

        def move(self):
            if (self.yloc < 0):
                self.yloc = max(0, self.yloc + self.speed)
            elif (self.yloc > (screen_height - paddle_height)):
                self.yloc = min(screen_height - paddle_height, self.yloc + self.speed)
            else:
                self.yloc = self.yloc + self.speed

        def get_rect(self):
            return pygame.Rect(self.xloc, self.yloc, paddle_width, paddle_height)

    class Ball():
        def __init__(self):
            self.speed = initial_ball_speed * multiplyer
            self.xloc = screen_width/2
            self.yloc = screen_height/2
            self.velocity = [multiplyer * initial_ball_speed * (math.cos((random.random() * math.pi/2) - math.pi/4)), multiplyer * initial_ball_speed * (math.sin((random.random() * math.pi/2) - math.pi/4))]
            self.hit_count = 0

        def check_if_hit(self, player):
            if ((self.yloc + ball_size) > player.yloc) | (self.yloc < (player.yloc + paddle_height)):
                self.hit_count += 1
                return True
            else:
                return False

        def hit_change_speed(self, player):
            m = math.pi/(2 * (paddle_height + ball_size))
            c = math.pi/4 - (math.pi * (player.yloc + paddle_height))/(2 * (paddle_height + ball_size))
            θ = m * self.yloc + c
            if player.xloc < screen_width/2:
                self.velocity = [self.speed * math.cos(θ), self.speed * math.sin(θ)]
            else:
                self.velocity = [-self.speed * math.cos(θ), self.speed * math.sin(θ)]

        def move(self):
            self.xloc = self.xloc + self.velocity[0]
            if (self.yloc + self.velocity[1] > (screen_height - ball_size)):
                self.yloc = screen_height - ball_size
                self.velocity[1] = -self.velocity[1]
            elif (self.yloc + self.velocity[1] < 0):
                self.yloc = 0
                self.velocity[1] = -self.velocity[1]
            else:
                self.yloc = self.yloc + self.velocity[1]

        def get_rect(self):
            return pygame.Rect(self.xloc, self.yloc, ball_size, ball_size)

    
    player1 = Player(30)
    player2 = Player(screen_width - 30)
    players = [player1, player2]
    ball = Ball()

    while (True):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()

            if e.type == pygame.KEYDOWN:
                match e.key:
                    case pygame.K_DOWN:
                        player2.change_speed(initial_player_speed * multiplyer)
                    case pygame.K_UP:
                        player2.change_speed(-initial_player_speed * multiplyer)
                    case pygame.K_w:
                        player1.change_speed(-initial_player_speed * multiplyer)
                    case pygame.K_s:
                        player1.change_speed(initial_player_speed * multiplyer)
                    
            if e.type == pygame.KEYUP:
                match e.key:
                    case pygame.K_DOWN:
                        player2.change_speed(0)
                    case pygame.K_UP:
                        player2.change_speed(0)
                    case pygame.K_w:
                        player1.change_speed(0)
                    case pygame.K_s:
                        player1.change_speed(0)

        game_screen.fill(black)
        for player in players:
            player.move()
            r = player.get_rect()
            pygame.draw.rect(game_screen, white, r)

        if ball.velocity[0] < 0:
            if (ball.xloc < (player1.xloc + paddle_width)) & (ball.xloc > player1.xloc):
                if ball.check_if_hit(player1):
                    ball.hit_change_speed(player1)
        elif ball.velocity[0] > 0:
            if (ball.xloc + ball_size > player2.xloc) & (ball.xloc + ball_size < player2.xloc + paddle_width):
                if ball.check_if_hit(player2):
                    ball.hit_change_speed(player2)

        ball.move()
        r = ball.get_rect()
        pygame.draw.rect(game_screen, white, r)

        if ball.hit_count % 6 == 5:
            multiplyer += 1
            ball.hit_count += 1

        if ball.xloc > screen_width:
            player1.score += 1
            multiplyer = 5
            ball.hit_count = 0
            parity = player1.score + player2.score
            ball.velocity = [((-1)**(parity))*multiplyer * initial_ball_speed * (math.cos((random.random() * math.pi/2) - math.pi/4)), multiplyer * initial_ball_speed * (math.sin((random.random() * math.pi/2) - math.pi/4))]
            ball.xloc = screen_width/2
            ball.yloc = screen_height/2
        elif ball.xloc < -ball_size:
            player2.score += 1
            multiplyer = 5
            ball.hit_count = 0
            parity = player1.score + player2.score
            ball.velocity = [((-1)**(parity))*multiplyer * initial_ball_speed * (math.cos((random.random() * math.pi/2) - math.pi/4)), multiplyer * initial_ball_speed * (math.sin((random.random() * math.pi/2) - math.pi/4))]
            ball.xloc = screen_width/2
            ball.yloc = screen_height/2

        pygame.display.update()
        clock.tick(60)

    #Define the player classes.
    #Initial x for each side. Give each one a fixed speed. Note position.
    #Move function.
    #Change speed function.

    #Define the ball class
    #Attributes are: speed, velocity, position, in_goal_A, in_goal_B, hit_count
    #Functions: check if intersecting with a given thing (and will change speed accordingly. speed increases with hit_count
    #         : move function (which will edit speed if it has bumped into an edge)

if __name__ == "__main__":
    main()