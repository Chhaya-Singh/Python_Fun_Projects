import turtle
my_pen=turtle.Turtle()
my_pen.shape("arrow")
turtle.bgcolor("orchid")
my_pen.color("black")

for i in range(0,15):
    x_from=0
    y_from=(14-i)*20
    x_to=i*20
    y_to=0
    my_pen.penup()
    my_pen.goto(x_from,y_from)
    my_pen.pendown()
    my_pen.goto(x_to,y_to)

for i in range(0,15):
    x_from=0
    y_from=(-14+i)*(-20)
    x_to=i*(-20)
    y_to=0
    my_pen.penup()
    my_pen.goto(x_from,y_from)
    my_pen.pendown()
    my_pen.goto(x_to,y_to)

for i in range(0,15):
    x_from=0
    y_from=(-14+i)*(-20)
    x_to=i*(-20)
    y_to=0
    my_pen.penup()
    my_pen.goto(x_from,y_from)
    my_pen.pendown()
    my_pen.goto(x_to,y_to)

for i in range(0,15):
    x_from=0
    y_from=(-14+i)*(-20)
    x_to=i*(-20)
    y_to=0
    my_pen.penup()
    my_pen.goto(x_from,y_from)
    my_pen.pendown()
    my_pen.goto(x_to,y_to)

my_pen.hideturtle()
turtle.done()