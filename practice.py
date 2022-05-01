from turtle import Turtle,Screen
turtle = Turtle(shape="square")
screen = Screen()
def ahead():
    turtle.forward(20)
def back1():
    turtle.backward(20)
def left1():
    turtle.left(90)
screen.listen()
screen.onkey(key="space",fun=ahead)
screen.onkey(key="b",fun=back1)
screen.onkey(key="l",fun=left1)

screen.exitonclick()












# from turtle import Turtle,Screen
# turtle = Turtle(shape="square")
# screen = Screen()
# screen.setup(width=600,height=600)
# screen.title("My Snake Game")
# screen.bgcolor("black")
# turtle.color("white")
# # for _ in range(10):
# #     turtle.forward(20)
# #     screen.delay(1000)
#
# screen.tracer(8,25)
# dist = 2
# for i in range(20):
#     turtle.speed(1)
#     turtle.fd(dist)
#     turtle.rt(90)
#     screen.delay(500)
#     dist += 2
# screen.exitonclick()