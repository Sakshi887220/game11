"""Cannon, hitting targets with projectiles.
"""

from random import randrange
from turtle import *
from base import vector

# ball is a vector object it gives the position of the ball
ball = vector(-200, -200)
# speed is the magnitude an direction in which ball will move
# Initial speed of tje ball is 0
speed = vector(0, 0)
targets = []

# take the vector object and returns whether it is inside the screen or not
def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

# Tap function if for the condition that there can be only hitting ball on our screen
def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 300) / 25
        speed.y = (y + 300) / 25

# Function for drawing all the balls on the screen
def draw():
    "Draw ball and targets."
    # clear all balls in previous loop
    clear()
    # targets are in a global list they will be drawn again
    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')
    #every time new position of the hiiting ball will show up removing the older one
    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    #update()
 # This is the main function 
def move():
    "Move ball and targets."
    # Introducing new target balls
    # As move function is called after every 50 ms so we can not append after each 50 ms because then there will be soo many target balls
    # So we have applied a condition that randrange(40) == 0
    if randrange(40) == 0:
        y = randrange(-150, 150)
        # Make a new target and append it to global list of targets
        target = vector(200, y)
        targets.append(target)
    # Move each target by 0.5 to the left
    for target in targets:
        target.x -= 0.5

    # condition for projectile motion of out hitting ball after every 50 ms 0.5 velocity is decreased in 
    if inside(ball):
        speed.y -= 0.5
        ball.move(speed)

    # if our hitting ball hits the target ball we need to remove target ball
    # first we create a duplicate list
    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        # distance between the target and hitting if it greater than a threshold value we assume it to be safe and append to our target list otherwise we discard it.
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    # condition for game to finish. If any target ball gets out of the screen we lose the game.
    for target in targets:
        if not inside(target):
            return
    # move function will be called after every 50 ms
    ontimer(move, 50)

#Setup screen with dimension 420*420
setup(420, 420)

#Hides the turtle
hideturtle()
up()

#Delays animation if turned on
tracer(False)
# As we click on the screen onscreenclick returns the coordinates of the cursor where we click it and those coordinates are passed to tap function.
# Note that we didn't called the function tap rather we just called an reference of our function
onscreenclick(tap)
move()
done()
