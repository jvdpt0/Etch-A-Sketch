from turtle import Turtle, Screen


def move_forwards():
    tt.fd(10)


def move_backwards():
    tt.bk(10)


def turn_right():
    tt.rt(10)


def turn_left():
    tt.lt(10)


def restart():
    tt.reset()


screen = Screen()
tt = Turtle()
screen.listen()
screen.onkey(key='w', fun=move_forwards)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key='c', fun=restart)
screen.exitonclick()
