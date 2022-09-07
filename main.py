from turtle import Screen, Turtle
from paddle import Paddle
from tiles import Tiles
from ball import Ball
from scoreboard import Scoreboard
import time
score = Scoreboard()
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle((10, -280))
tiles = Tiles()

global ball
ball = Ball()
ball.reset_position()

# scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()
    #check for walls
    print(f'y = {ball.ycor()}')
    # if ball.xcor() > 130 or ball.xcor() < -130:
    if ball.xcor() > 379 or ball.xcor() < -386:
        ball.bounce_x()

    if ball.ycor() > 260:
        ball.bounce_y()

    if ball.ycor() < -290:
        print("game over")
        game_is_on = False

    #detect colision with paddle
    if ball.distance(paddle) < 35:
        ball.bounce_y()

    for i in tiles.all_tiles:
        print(len(tiles.all_tiles))
        if ball.distance(i) < 35:
            i.ht()
            tiles.all_tiles.remove(i)
            ball.bounce_y()
            score.point()
#     #Detect collision with wall
#     if ball.ycor() > 280 or ball.ycor() < -280:
#         ball.bounce_y()
#
#     #Detect collision with paddle
#     if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
#         ball.bounce_x()
#
#     #Detect R paddle misses
#     if ball.xcor() > 380:
#         ball.reset_position()
#         scoreboard.l_point()
#
#     #Detect L paddle misses:
#     if ball.xcor() < -380:
#         ball.reset_position()
#         scoreboard.r_point()

screen.exitonclick()