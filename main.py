from turtle import Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Score

import time
# setting up the stage
screen = Screen()
screen.setup(850, 650)
screen.screensize(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# creating the  pong ball and the paddles
score = Score()
ball = Ball()
r_paddle = Paddle(400)
l_paddle = Paddle(-400)

# detect Movement of ball and paddle
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with bottom and top wall
    if ball.ycor() > 290 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 370 or ball.distance(l_paddle) < 50 and ball.xcor() < -370:
        ball.bounce_x()

    # detect when paddle misses ball
    if ball.distance(r_paddle) > 50 and ball.xcor() > 420:
        ball.reset_position()
        score.point_l()
        score.update_score()

    elif ball.distance(l_paddle) > 50 and ball.xcor() < -420:
        ball.reset_position()
        score.point_r()
        score.update_score()

    # calculate score
    if score.r_player_score == 2:
        score.goto(0, 0)
        score.write("Right player wins", align="center", font=("Courier", 80, "normal"))
        game_is_on = False
    elif score.l_player_score == 2:
        score.goto(0, 0)
        score.write("Left player wins", align="center", font=("Courier", 80, "normal"))
        game_is_on = False

screen.exitonclick()

