from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.title("My Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # detect food and scoreboard increases
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extends()

    # detect collision ( hit wall )
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        game_is_on = False
        scoreboard.game_over()

    # collision with tails then game over
    for seg in snake.segments:
        if seg == snake.head:
            pass
        elif snake.head.distance(seg) < 10:
            game_is_on = False
            scoreboard.game_over()

    # if you want to write less code for above condition the use slicing
    # for seg in snake.segments[1:]:
    #     if snake.head.distance(seg) < 10:
    #         game_is_on = False
    #         scoreboard.game_over()

screen.exitonclick()




