import turtle
tt=turtle.Turtle()

def up():
    tt.setheading(90)
    tt.forward(100)

def left():
    tt.setheading(180)
    tt.forward(100)

def right():
    tt.setheading(0)
    tt.forward(100)

def down():
    tt.setheading(270)
    tt.forward(100)


turtle.listen()
turtle.onkey(up,"Up")
turtle.onkey(down,"Down")
turtle.onkey(left,"Left")
turtle.onkey(right,"Right")
turtle.mainloop()