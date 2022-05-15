import pygame
from paddle import Paddle
from ball import Ball
from brick import Brick
from Powerup import powerup
 
pygame.init()
 
# Define some colors
WHITE = (255,255,255)
BLUE = (0, 0, 255)
RED = (255,0,0)
ORANGE = (255,100,0)
YELLOW = (255,255,0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
GREY = (255, 255, 255)

score = 0
lives = 3
 
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout Game")

all_sprites_list = pygame.sprite.Group()
 
paddle = Paddle(WHITE, 100, 10)
paddle.rect.x = 350
paddle.rect.y = 560
 
#Create the ball sprite
ball = Ball(WHITE,10,10)
ball.rect.x = 345
ball.rect.y = 195

#Create the Powerup sprite
all_powerup = pygame.sprite.Group()
powerup = powerup(GREY, 10, 10)
powerup.rect.x = 346
powerup.rect.y = 196

all_bricks = pygame.sprite.Group()
for i in range(8):
    brick = Brick(RED, 80, 30)
    brick.rect.x = 35 + i* 92.5
    brick.rect.y = 60
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(8):
    brick = Brick(ORANGE, 80, 30)
    brick.rect.x = 35 + i* 92.5
    brick.rect.y = 95
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(8):
    brick = Brick(YELLOW, 80, 30)
    brick.rect.x = 35 + i* 92.5
    brick.rect.y = 130
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(8):
    brick = Brick(GREEN, 80, 30)
    brick.rect.x = 35 + i* 92.5
    brick.rect.y = 165
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(8):
    brick = Brick(BLUE, 80, 30)
    brick.rect.x = 35 + i* 92.5
    brick.rect.y = 200
    all_sprites_list.add(brick)
    all_bricks.add(brick)
 
all_sprites_list.add(paddle)
all_sprites_list.add(ball)
all_sprites_list.add(powerup)

carryOn = True
 
clock = pygame.time.Clock()
 
while carryOn:
    # --- Main event loop
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
              carryOn = False 
 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        paddle.moveRight(5)
 
    all_sprites_list.update()
 
    if ball.rect.x>=790:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>590:
        ball.velocity[1] = -ball.velocity[1]
        lives -= 1
        if lives == 0:
            font = pygame.font.Font(None, 74)
            text = font.render("GAME OVER", 1, WHITE)
            screen.blit(text, (250,300))
            pygame.display.flip()
            pygame.time.wait(3000)
 
            #Stop the Game
            carryOn=False
 
    if ball.rect.y<40:
        ball.velocity[1] = -ball.velocity[1]
 
    #Detect collisions between the ball and the paddles
    if pygame.sprite.collide_mask(ball, paddle):
      ball.rect.x -= ball.velocity[0]
      ball.rect.y -= ball.velocity[1]
      ball.bounce()
 
    #Check if there is the ball collides with any of bricks
    brick_collision_list = pygame.sprite.spritecollide(ball,all_bricks,False)
    for brick in brick_collision_list:
      ball.bounce()
      score += 1
      brick.kill()
      if brick.kill:
          from Powerup import powerup
          from random import randint
          i = randint(1, 10)
          if i == 2:
              powerup(GREY, 10, 10)


      if len(all_bricks)==0:
           #Display Level Complete Message for 3 seconds
            font = pygame.font.Font(None, 74)
            text = font.render("LEVEL COMPLETE", 1, WHITE)
            screen.blit(text, (200,300))
            pygame.display.flip()
            pygame.time.wait(3000)
 
            #Stop the Game
            carryOn=False
 
    # --- Drawing code should go here
    # First, clear the screen to dark blue.
    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, [0, 38], [800, 38], 2)
 
    #Display the score and the number of lives at the top of the screen
    font = pygame.font.Font(None, 34)
    text = font.render("Score: " + str(score), 1, WHITE)
    screen.blit(text, (20,10))
    text = font.render("Lives: " + str(lives), 1, WHITE)
    screen.blit(text, (650,10))
 
    #Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
    all_sprites_list.draw(screen)
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
#Once we have exited the main program loop we can stop the game engine:
pygame.quit()