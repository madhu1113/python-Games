

# Spaceship Bullet  game using pygame


import pygame
import os
pygame.font.init()
pygame.mixer.init()

# All the constant values in capslock which will be same throughout the program.
WIDTH, HEIGHT = 900, 500                    # Width and Height of the Screen
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # Set the window or screen
pygame.display.set_caption("Spaceship Bullet Game")     # title of game

WHITE = (255, 255, 255)                 # RGB Code of white color
BLACK = (0, 0, 0)                        # RGB Code of black color for middle boundary
RED = (255, 0, 0)                         # RGB Code of red color for red bullet
YELLOW = (255, 255, 0)                     # RGB Code of yellow color for yellow bullet

BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)       # Border in between screen

BULLET_HIT_SOUND = pygame.mixer.Sound('Assets/Grenade+1.mp3') # load the Bullet hit sound
BULLET_FIRE_SOUND = pygame.mixer.Sound('Assets/Gun+Silencer.mp3') # load the bullet fire sound

HEALTH_FONT = pygame.font.SysFont('comicsans', 40) # Health Score board font type and Size
WINNER_FONT = pygame.font.SysFont('comicsans', 100) # After game gets over winner font type and size

FPS = 60                    # frame per second game has to be updated
VEL = 5                        # Velocity of spaceship
BULLET_VEL = 7              # Velocity of Bullet
MAX_BULLETS = 3              # Max Bullet on screen
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40      # Spaceship width and height

YELLOW_HIT = pygame.USEREVENT + 1       
RED_HIT = pygame.USEREVENT + 2

YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_yellow.png'))     # Load the yellow spaceship image
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)    # resize and rotate the yellow spaceship at 90 degree.

RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))        # Load the red spaceship image
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270) # resize and red rotate the spaceship at 90 degree.

SPACE = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT)) # load and scale the background image.


def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    WIN.blit(SPACE, (0, 0))
    pygame.draw.rect(WIN, BLACK, BORDER)        # Draw the black border in Middle of screen

    red_health_text = HEALTH_FONT.render(
        "Health: " + str(red_health), 1, WHITE)     # red  Spaceship health scoreboard at right up corner
    yellow_health_text = HEALTH_FONT.render(
        "Health: " + str(yellow_health), 1, WHITE)      # yellow Spaceship health scoreboard at left up corner
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10)) # display red health scoreboard
    WIN.blit(yellow_health_text, (10, 10))      # Display yello health scoreboard

    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))    # Display the yellow spaceship on screen at x and y coordinate.
    WIN.blit(RED_SPACESHIP, (red.x, red.y))         # Display the red spaceship on screen at x and y coordinate.

    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)      # Dispay the red bullet

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)   # Display the yellow bullet

    pygame.display.update()

# Movement of yellow spaceship
def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:  # yellow spaceship moves to left by pressing a in keyboard and shouldn't go out of screen
        yellow.x -= VEL                 # decrease the x coordinate by 5 px
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x:  # RIGHT movement by pressing d and shouldn't go out of boundary
        yellow.x += VEL                
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:  # moves up by pressong w and shouldn't go out of screen.
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 15:  # Moves down by pressing s and shouldn't go out of screen
        yellow.y += VEL

# Movement of red spaceship
def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width:  # move left by pressing left arrow and shouldn't go out of boundary 
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH:  # move right by pressing right arrow and shouldn't go out of screen
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:  # move up by pressing up arrow and should't go out of screen.
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 15:  # move down by pressing down arrow shouldn't go out of screen.
        red.y += VEL

# Fire the bullets
def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL          # Move yellow bullet in right dirn.
        if red.colliderect(bullet):         # If yellow bullet collides to red spaceship
            pygame.event.post(pygame.event.Event(RED_HIT)) # call the red hit event
            yellow_bullets.remove(bullet)           # Remove the yellow bullet once it hits the red spaceship
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)       #else remove the yellow bullet once it reaches to the edge of screen

    for bullet in red_bullets:
        bullet.x -= BULLET_VEL          # Move red bullet in left direction
        if yellow.colliderect(bullet):  # If red bullets collide with yellow spaceship
            pygame.event.post(pygame.event.Event(YELLOW_HIT))       
            red_bullets.remove(bullet)      # Remove the red bullet
        elif bullet.x < 0:
            red_bullets.remove(bullet)      # else remove the red bullet once it reaches to the left edge of screen


def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width() /
                         2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)


def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)  # position of red rectangle
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)   # position of yellow rectange

    red_bullets = []            # List of red bullets
    yellow_bullets = []            # List of yellow bullets

    red_health = 10             
    yellow_health = 10

    clock = pygame.time.Clock()         # create an obkect of Clock 
    run = True
    while run:
        clock.tick(FPS)                         # Frame gets updated every 60s.     
        for event in pygame.event.get():        # Loop through the list of different events.
            if event.type == pygame.QUIT:       # If user close the window
                run = False                     # Stop the game
                pygame.quit()                   # Quit the game

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

                if event.key == pygame.K_RSHIFT and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        red.x, red.y + red.height//2 - 2, 10, 5)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

            if event.type == RED_HIT:       # If red hets hit by yellow
                red_health -= 1     # red health will decrease by -1
                BULLET_HIT_SOUND.play() # play the hit sound

            if event.type == YELLOW_HIT:        # If yello spaceship gets hit
                yellow_health -= 1          # yellow health decrease by 1
                BULLET_HIT_SOUND.play()     # Play the hit sound

        winner_text = ""
        if red_health <= 0:             # condition of yellow wins when red<=0
            winner_text = "Yellow Wins!"

        if yellow_health <= 0:              # # condition of red wins when yellow<=0
            winner_text = "Red Wins!"

        if winner_text != "":
            draw_winner(winner_text)
            break

        keys_pressed = pygame.key.get_pressed()         # object to get the state of all keyboard buttons.
        yellow_handle_movement(keys_pressed, yellow)    # Call the yellow_handle_movement()
        red_handle_movement(keys_pressed, red)          #  Call the red_handle_movement()

        handle_bullets(yellow_bullets, red_bullets, yellow, red) # Call the handle bullet function

        draw_window(red, yellow, red_bullets, yellow_bullets,
                    red_health, yellow_health)      # Call the draw window function

  


if __name__ == "__main__":      
    main()                      # To run the file directly rather than imported from somewhere else
