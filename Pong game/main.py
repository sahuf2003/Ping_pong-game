from turtle import Screen
from ball import Ball
from paddle import Paddle
import time
from scoreboard import Scoreboard
screen = Screen()
screen.title("Pong game")
screen.setup(height=600,width=800)
screen.bgcolor("black")
screen.tracer(0)

r_paddle= Paddle()
l_paddle = Paddle()
l_paddle.goto(-390,0)
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 40 and ball.xcor() > 320 or ball.xcor() < -320 and ball.distance(l_paddle) < 40:
        ball.bounce_x()
    if ball.xcor() > 390:
        scoreboard.l_point()
        ball.reset_position()
    if ball.xcor() < -390:
        scoreboard.r_point()
        ball.reset_position()
screen.exitonclick()
