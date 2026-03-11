import turtle
t=turtle.Screen()
t.bgcolor("lightblue")
t.setup(500,300)
t.title("Welcome to Turle")
board=turtle.Turtle()
board.speed(1)
for i in range (4):
    board.forward(100)
    board.left(90)
turtle.done()