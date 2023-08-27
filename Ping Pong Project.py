# A simple pingpong project

import turtle

# setting up the window
window = turtle.Screen()    # this returns a screen
window.setup(width=800, height=600)    # setting up the window size
window.bgcolor("black")   # setting up the background color
window.title("Ping Pong Game by karim")   # the line that appears at the top of the window
window.tracer(0)    # stopping the window from updating itself

# creating racket1
racket1 = turtle.Turtle()   # creating a turtle object
racket1.shape("square")    # identifying the shape of the racket
racket1.shapesize(stretch_wid=5, stretch_len=1)   # stretching the shape size, height -->20*5Px and width -->1*20Px
racket1.color("red")    # setting the color of the shape
racket1.penup()    # prevening the racket from making any lines
racket1.goto(-350, 0)    # setting the location of the racket
racket1.speed(0)   # setting the speed at which the screen updating the racket when moving (Animation speed)

# creating racket2
racket2 = turtle.Turtle()
racket2.shape("square")
racket2.shapesize(stretch_wid=5, stretch_len=1)
racket2.color("blue")
racket2.penup()
racket2.goto(350, 0)
racket2.speed(0)

# creating the ball
ball = turtle.Turtle()
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.15   # setting the speed at which the ball moves
ball.dy = 0.15
ball.speed(0)

# creating the score
score = turtle.Turtle()
score.color("gray")
score.penup()
score.goto(0, 260)
score.speed(0)
score.hideturtle()   # hiding the unwanted shape of the turtle object
score1 = 0   # setting the initial value of score1
score2 = 0   # setting the initial value of score2

# creating the result
result = turtle.Turtle()
result.color("green")
result.penup()
result.goto(0, 240)
result.speed(0)
result.hideturtle()


# functions
def rack1_up():  # A function to move the racket1 up
    y = racket1.ycor()   # getting the y coordinates
    y += 30      # increasing the y by 30, the amount that the racket will be moving
    racket1.sety(y)   # updating y with the new value


def rack1_down():   # A function to move the racket1 down
    y = racket1.ycor()
    y -= 30
    racket1.sety(y)


def rack2_up():    # A function to move the racket2 up
    y = racket2.ycor()
    y += 30
    racket2.sety(y)


def rack2_down():   # A function to move the racket2 down
    y = racket2.ycor()
    y -= 30
    racket2.sety(y)


# keyboard Bindings
window.listen()   # prepare the window for receiving any presses
window.onkeypress(rack1_up, "w")   # on pressing the key "w" call the "rack1_up" function
window.onkeypress(rack1_down, "s")   # on pressing the key "s" call the "rack1_down" function
window.onkeypress(rack2_up, "Up")     # on pressing the up key call the "rack2_up" function
window.onkeypress(rack2_down, "Down")    # on pressing the down key call the "rack2_down" function

while True:
    window.update()   # keep updating the screen

    # moving the ball
    ball.setx(ball.xcor() + ball.dx) # increasing the x coordinate by the dx value ,so it moves
    ball.sety(ball.ycor() + ball.dy)

    # border check
    if ball.ycor() > 290:  # checking if the ball is hitting the upper border
        ball.sety(290)
        ball.dy *= -1   # moving the ball in the opposite direction

    if ball.ycor() < -290:  # checking if the ball is hitting the down border
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 430:  # checking if the ball is hitting the right border
        ball.goto(0, 0)   # setting the border into the middle
        ball.dx *= -1
        score1 += 1    # increasing the score1 by one
        result.clear()  # clearing the result text from the screen
        score.clear()   # clearing the score text from the screen
        if score1 == 3: # checking if the score1 reach 3, then player 1 wins, and reset the game score.
            result.write("Player1 Won!", align="center", font="Carrier")
            score1 = 0
            score2 = 0
            ball.goto(0,0)

        score.write("Player1: {}, Player2: {}".format(score1,score2), align="center", font="Carrier")

    if ball.xcor() < -430:     # checking if the ball is hitting the left border
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        result.clear()
        score.clear()
        if score2 == 3:
            result.write("Player2 Won!", align="center", font="Carrier")
            score1 = 0
            score2 = 0
            ball.goto(0, 0)

        score.write("Player1: {}, Player2: {}".format(score1, score2), align="center", font="Carrier")

    if (racket1.xcor() + 10 > ball.xcor() > racket1.xcor()) and    # cheking if the ball hits the racket1 then make it go back
    (racket1.ycor() + 40 >= ball.ycor() >= racket1.ycor() - 40):

        ball.setx(-340)
        ball.dx *= -1

    if (racket2.xcor() + 10 > ball.xcor() > racket2.xcor() - 10) and    # cheking if the ball hits the racket2 then make it go back
    (racket2.ycor() + 40 >= ball.ycor() >= racket2.ycor() - 40):

        ball.setx(340)
        ball.dx *= -1
