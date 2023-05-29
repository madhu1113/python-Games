# pong game using turtle

import turtle
import os

wn = turtle.Screen()    # To start a Screen
wn.title("Pong by @madhu")
wn.bgcolor("black")        #Change the background color to black
wn.setup(width = 800, height = 600)         #Set the screen Size (0.0) is in the center (300, -300) up and down of screen and (400, -400) right and left of screen boundary.
wn.tracer(0)            #Stops the window from updating. Basically speedup our game little bit


# Score
score_a = 0
score_b = 0


# Paddle A
paddle_a = turtle.Turtle()  # object of Turtle class
paddle_a.speed(0)           # It's not the speed paddle moves on the screen. It Sets the speed to the max possible speed else it will be very slow.
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_a.penup()
paddle_a.goto(-350,0)                   # Left dimension -350

# Paddle B
paddle_b = turtle.Turtle()  # create a padle_b object of Turtle class
paddle_b.speed(0)           # It's not the speed paddle moves on the screen. It Sets the speed to the max possible speed else it will be very slow.
paddle_b.shape("square")        # Paddle shape is square
paddle_b.color("white")         
paddle_b.shapesize(stretch_wid = 5, stretch_len = 1)        # Stretch the paddle which is now 5*20=100 pixel height and 20 pixel wide
paddle_b.penup()
paddle_b.goto(350,0)            # Right dimesion is +350


# Ball
ball = turtle.Turtle()  # create a ball object
ball.speed(0)           
ball.shape("square")        # By defalult ball dimension is 20*20
ball.color("white")                
ball.penup()
ball.goto(0,0)    # Ball should start from middle

# Ball Movement to up right i.e digonally
ball.dx = 2     # Change of x-axis by 2 pixel i.e right side
ball.dy = -2        # Change of y-axis by 2 pixel i.e up side

# For Scoring use pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()             # Since we don't want to draw a line when pen moves
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A : 0   Player B: 0", align= "center", font = ("Courier", 24, "normal"))





# Functions to move the paddle

# Left paddle To move up
def paddle_a_up():
    y = paddle_a.ycor()     # get the y-coordiane of paddle_a 
    y += 20                    # increase the paddle_a y-coordiane to 20 pixel. Since 1 block is of 20 pixel.
    paddle_a.sety(y)        # set the paddle_a to new y

# Left paddle to move down
def paddle_a_down():
    y = paddle_a.ycor()     # get the y-coordiane of paddle_a 
    y -= 20                    # increase the paddle_a y-coordiane to 20 pixel.
    paddle_a.sety(y) 

# Right paddle To move up
def paddle_b_up():
    y = paddle_b.ycor()     # get the y-coordiane of paddle_b 
    y += 20                    # increase the paddle_b y-coordiane to 20 pixel.
    paddle_b.sety(y)  

# Right paddle To move down
def paddle_b_down():
    y = paddle_b.ycor()     # get the y-coordiane of paddle_b
    y -= 20                    # increase the paddle_b y-coordiane to 20 pixel.
    paddle_b.sety(y) 


# Keyboard binding to call the function through keyboard
wn.listen()                         # listen for keyboard input
wn.onkeypress(paddle_a_up, "w")     # When user press "w" call the paddle_a_up() function
wn.onkeypress(paddle_a_down, "s")      # When user press "s" call the paddle_a_up() function
wn.onkeypress(paddle_b_up, "Up")     # When user press "up arrow" call the paddle_b_up() function
wn.onkeypress(paddle_b_down, "Down")    #When user press "down arrow" call the paddle_b_down() function


# Main game loop
while True:
    wn.update()             # updates the screen everytime loop runs
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking--> up side
    if ball.ycor() > 290:     # If call reaches to boundary
        ball.sety(290)      # don't move
        ball.dy *= -1       # Revert back
        os.system("afplay bounce.wav&")         # Add & at the end else screen stucks after sound

    # Border Checking--> down side
    if ball.ycor() < -290:     # If call reaches to boundary
        ball.sety(-290)      # don't move
        ball.dy *= -1       # Revert back
        os.system("afplay bounce.wav&") 

    # Border Checking--> Right side
    if ball.xcor() > 390:
        ball.goto(0, 0)            # If it hits the Right wall again start from middle
        ball.dx *= -1
        score_a += 1            # when player B losses Player A gets the score+1
        pen.clear()
        pen.write("Player A : {}   Player B: {}".format(score_a, score_b), align= "center", font = ("Courier", 24, "normal"))

    # Border Checking--> Left side
    if ball.xcor() < -390:
        ball.goto(0, 0)            # If it hits the left wall again start from middle
        ball.dx *= -1
        score_b += 1 
        pen.clear()
        pen.write("Player A : {}   Player B: {}".format(score_a, score_b), align= "center", font = ("Courier", 24, "normal"))

    # paddle and ball collision
    if(ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        os.system("afplay bounce.wav&") 

    if(ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        os.system("afplay bounce.wav&") 





