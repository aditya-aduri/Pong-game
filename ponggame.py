# pong game
import turtle

window = turtle.Screen()
window.title("Pong Game 2.0")
window.bgcolor("red")
window.setup(width=800, height=600)  # to setup the width and height
window.tracer()  # for manual update of the game

#scores of players
score_a = 0
score_b = 0

# bar A
bar_a = turtle.Turtle()
bar_a.speed(0)
bar_a.shape("square")
bar_a.color("black")
bar_a.shapesize(stretch_wid=5, stretch_len=1)
bar_a.penup()  # we dont need to draw line thats why we use penup
bar_a.goto(-350, 0)

# bar B
bar_b = turtle.Turtle()  # BECAUSE ITS AN OBJECT
bar_b.speed()
bar_b.shape("square")
bar_b.color("black")
bar_b.shapesize(stretch_wid=5, stretch_len=1)
bar_b.penup()  # we dont need to draw line thats why we use penup
bar_b.goto(+350, 0)

# ball
ball = turtle.Turtle()  # BECAUSE ITS AN OBJECT
ball.speed(0)
ball.shape("square")
ball.color("black")
ball.penup()  # we dont need to draw line thats why we use penup
ball.goto(0, 0)
ball.dx = 4
ball.dy = -4

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("PLAYER A : 0      PLAYER B : 0", align="center", font=("Courier", 24, "bold"))


# Function
def bar_a_up():
    y = bar_a.ycor()
    y += 20
    bar_a.sety(y)


def bar_a_down():
    y = bar_a.ycor()
    y -= 20
    bar_a.sety(y)


def bar_b_up():
    y = bar_b.ycor()
    y += 20
    bar_b.sety(y)


def bar_b_down():
    y = bar_b.ycor()
    y -= 20
    bar_b.sety(y)


# keys
window.listen()
window.onkey(bar_a_up, "w")
window.onkey(bar_a_down, "s")
window.onkey(bar_b_up, "8")
window.onkey(bar_b_down, "5")

# main game play
while True:
    window.update()  # this will update the screen on each repetation of the screen

    #moving ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    #borders
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        #to add audio use os.system("afplay sound.wav&)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("PLAYER A : {}      PLAYER B : {}".format(score_a, score_b), align="center", font=("Courier", 24, "bold"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("PLAYER A : {}      PLAYER B : {}".format(score_a, score_b), align="center", font=("Courier", 24, "bold"))


    #collision of ball and the bar
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < bar_b.ycor() + 40 and ball.ycor() > bar_b.ycor() -40) :
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < bar_a.ycor() + 40 and ball.ycor() > bar_a.ycor() -40) :
        ball.setx(-340)
        ball.dx *= -1


