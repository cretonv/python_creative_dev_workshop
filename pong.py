import turtle
import random
import time

delay = 0.005
ballXSpeed = 10
ballYSpeed = 10

racketHeight = 150
racketSpeed = 30

magicSpeed = 10
global magicDirection
magicDirection = "right"

# score
lScore = 0
rScore = 0

# set up the screen
win = turtle.Screen()
win.title('Un jeu super génial')
win.bgcolor("black")
win.setup(width=1200, height=800)
win.tracer(0)

# left player
lplayer = turtle.Turtle()
lplayer.speed(0)
lplayer.shape("square")
lplayer.color("darkviolet")
lplayer.penup()
lplayer.shapesize(racketHeight / 20, 0.5)
lplayer.goto(-550, 0)

# right player
rplayer = turtle.Turtle()
rplayer.speed(0)
rplayer.shape("square")
rplayer.color("mediumturquoise")
rplayer.penup()
rplayer.shapesize(racketHeight / 20, 0.5)
rplayer.goto(550, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("blueviolet")
ball.penup()
ball.goto(0, 0)

# Scores display
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 340)
pen.write("{}   |   {}".format(lScore, rScore), align="center", font=("Courier", 24, "normal"))

# Magic Turtle
magic = turtle.Turtle()
magic.speed(0)
magic.shape("turtle")
magic.color("#84FAF6")
magic.penup()
magic.goto(0, 370)

def lPlayer_go_up():
    if lplayer.ycor() < 400 - (racketHeight / 2):
        lplayer.direction = "up"
        y = lplayer.ycor()  # y coordinate of the turtle
        lplayer.sety(y + racketSpeed)


def lPlayer_go_down():
    if lplayer.ycor() > -400 + (racketHeight / 2):
        lplayer.direction = "down"
        y = lplayer.ycor()  # y coordinate of the turtle
        lplayer.sety(y - racketSpeed)

def rPlayer_go_up():
    if rplayer.ycor() < 400 - (racketHeight / 2):
        rplayer.direction = "up"
        y = rplayer.ycor()  # y coordinate of the turtle
        rplayer.sety(y + racketSpeed)


def rPlayer_go_down():
    if rplayer.ycor() > -400 + (racketHeight / 2):
        rplayer.direction = "down"
        y = rplayer.ycor()  # y coordinate of the turtle
        rplayer.sety(y - racketSpeed)


def moveBall():
    global ballYSpeed
    global ballXSpeed
    global lScore
    global rScore

    if ball.ycor() + ballYSpeed < -380 or ball.ycor() + ballYSpeed > 390:
        ballYSpeed = -ballYSpeed
    if ball.xcor() + ballXSpeed < -600 or ball.xcor() + ballXSpeed > 590:
        if ball.xcor() > 0:
            lScore += 1
            writeScore()
        else :
            rScore += 1
            writeScore()
        ballOut()
    if (ball.xcor() == lplayer.xcor() + 10 and (
            lplayer.ycor() + (racketHeight / 2) > ball.ycor() > lplayer.ycor() - (racketHeight / 2))) or (
            ball.xcor() == rplayer.xcor() - 10 and (
            rplayer.ycor() + (racketHeight / 2) > ball.ycor() > rplayer.ycor() - (racketHeight / 2))):
        ballXSpeed = -ballXSpeed
    if ((magic.ycor() - 50 >= ball.ycor()) and (ball.ycor() <= magic.ycor() + 50)) and ((magic.xcor() - 50 >= ball.xcor()) and (ball.xcor() <= magic.xcor() + 50)):
        giveBonus()


    ball.sety(ball.ycor() + ballYSpeed)
    ball.setx(ball.xcor() + ballXSpeed)

def moveMagic():
    global magicDirection

    if magicDirection == "right":
        magic.setx(magic.xcor() + magicSpeed)
    elif magicDirection == "bottom":
        magic.sety(magic.ycor() - magicSpeed)
    elif magicDirection == "top":
        magic.sety(magic.ycor() + magicSpeed)
    elif magicDirection == "left":
        magic.setx(magic.xcor() - magicSpeed)

    testMagicDirection()

def testMagicDirection():
    global magicDirection

    if magic.xcor() > 570 and magic.ycor() > 369:
        magicDirection = "bottom"
        rotateMagic()
    if magic.ycor() < -370 and magic.xcor() > 570:
        magicDirection = "left"
        rotateMagic()
    if magic.xcor() < -580 and magic.ycor() < -370:
        magicDirection = "top"
        rotateMagic()
    if magic.ycor() > 369 and magic.xcor() < -580:
        magicDirection = "right"
        rotateMagic()


def giveBonus():
    global rScore
    global lScore
    global magicDirection

    if(lScore > rScore):
        rScore += 10
    elif(lScore < rScore):
        lScore += 10

    magic.goto(0, 370)
    magicDirection = "right"

def rotateMagic():
    magic.right(90)


def increase_ball_speed():
    global ballYSpeed
    global ballXSpeed

    if ballYSpeed < 30 and ballXSpeed < 30:
        ballYSpeed = ballYSpeed * 1.1
        ballXSpeed = ballXSpeed * 1.1

def ballOut():
    ball.goto(0, 0)
    time.sleep(1)

def writeScore():
    pen.clear()
    pen.write("{}   |   {}".format(lScore, rScore), align="center", font=("Courier", 24, "normal"))

    if lScore > rScore:
        ball.color("darkviolet")
    elif lScore == rScore:
        ball.color("blueviolet")
    else:
        ball.color("mediumturquoise")

# keyboard bindings
win.listen()
win.onkey(lPlayer_go_up, "z")
win.onkey(lPlayer_go_down, "s")
win.onkey(rPlayer_go_down, "Down")
win.onkey(rPlayer_go_up, "Up")


# Main Game Loop
while True:
    win.update()
    moveBall()
    moveMagic()
