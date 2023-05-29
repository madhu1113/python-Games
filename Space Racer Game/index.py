# Space Racer Game using pyglet

import pyglet
import random

pyglet.resource.path = ["resources"]    # Provide the folder name where all resources are stored
pyglet.resource.reindex()

class AsteroidsWindow(pyglet.window.Window):            # passing pyglet Window class
    def __init__(self):                                 # Constructor
        super(AsteroidsWindow, self).__init__()         #The super() function returns an object that represents the parent class.

        
        self.keys = pyglet.window.key.KeyStateHandler()     # KeyStateHandler():-> To store the current keyboard state
        self.push_handlers(self.keys)                       # push onto the event handler

        self.set_caption("Space Race")                      # Caption for the window

        self.ship_image = pyglet.resource.image("alienblaster.png")     # load th ship image
        self.asteroid_image = pyglet.resource.image("asteroid.png")     # load the asteroid image
        
        self.center_image(self.ship_image)          
        self.center_image(self.asteroid_image)
        
        self.explosion_sound = pyglet.resource.media("bigbomb.wav", streaming=False)    # load the explosion sound
        self.background_music = pyglet.resource.media("cyber-soldier.wav", streaming=False)    # load the game music

        self.ship = pyglet.sprite.Sprite(img=self.ship_image, x=500, y=30) # Position of ship
        self.ship.scale = 0.5                       # Size of ship
        self.ship.rotation = 180               # ship should be upward pointed     

        self.score_label = pyglet.text.Label(text="Score:0 Highscore:0", x=10, y=10) # Position of Score
        self.score = 0      # initially score 0
        self.highscore = 0     #initially high score 0

        self.asteroids = [] # asteroid list
        self.stars = []     # stars list

        pyglet.clock.schedule_interval(self.game_tick, 0.005)       #call the game_tick() every 5 ms. and update the everything.
        self.background_music.play()                                #play the backgroung music
        pyglet.clock.schedule_interval(lambda x: self.background_music.play(), 13.8) # play the background music and every 13.8s

 # update all the component on screen
    def game_tick(self, dt):           
        self.update_stars()
        self.update_asteroids()
        self.update_ship()
        self.update_score()
        self.draw_elements()

    # display all the components
    def draw_elements(self):        
        self.clear()                # first clear the screen
        for star in self.stars:
            star.draw()             # for every star in list display the stars
        for asteroid in self.asteroids: 
            asteroid.draw()         # or every asteroid in list display the asteroids
        self.ship.draw()            # display the ship
        self.score_label.draw()     # Display the score label


    def update_stars(self):
        if self.score % 100 == 0:
            self.stars.append(pyglet.text.Label(text="*", x=random.randint(0, 800), y=600)) # Generate * randomly and add onto the stars list
        for star in self.stars:         # keep decreasing the star location by 20 pixel in y-axis
            star.y -= 20
            if star.y < 0:                  # if y location reaches to 0 remove the *
                self.stars.remove(star)

    def update_asteroids(self):
        if random.randint(0, 45) == 3:
            ast = pyglet.sprite.Sprite(img=self.asteroid_image, x=random.randint(0, 800), y=600) # Generate asteroid image randomly
            ast.scale = 0.3                 # Size of asteroids
            self.asteroids.append(ast)       # append randomly generated asteroid to list
        for asteroid in self.asteroids:
            asteroid.y -= 7
            if asteroid.y < 0:
                self.asteroids.remove(asteroid)     # Remove asteroid after reaching to the bottom of screen
        for asteroid in self.asteroids:
            if self.sprites_collide(asteroid, self.ship):   # If collision b/w ship and asteroid
                self.asteroids.remove(asteroid)             # Remove the asteroid
                self.score = 0                              # Make the score 0
                self.explosion_sound.play()                 # play the explosion sound

# left and right movement of ship
    def update_ship(self):
        if self.keys[pyglet.window.key.LEFT] and not self.ship.x < 0: # If press left arrow 
            self.ship.x -= 4                                    # shift the ship to 4 times to left side
        elif self.keys[pyglet.window.key.RIGHT] and not self.ship.x > 950: # # If press right arrow 
            self.ship.x += 4                        # shift the ship to 4 times to right side    

# Change of score and high score--> If score is more than high score then update high score
    def update_score(self):     
        self.score += 1
        if self.score > self.highscore:
            self.highscore = self.score
        self.score_label.text = "Score: %s Highscore: %s" % (self.score, self.highscore)

# Put the image in center
    def center_image(self, image):
        image.anchor_x = image.width/2
        image.anchor_y = image.height/2

# check for for collision--> If collides remove the asteroid
    def sprites_collide(self, spr1, spr2):
        return (spr1.x-spr2.x)**2 + (spr1.y-spr2.y)**2 < (spr1.width/2 + spr2.width/2)**2

game_window = AsteroidsWindow()     # object of AsteroidsWindow class
pyglet.app.run()                    #Call the pyglet app
