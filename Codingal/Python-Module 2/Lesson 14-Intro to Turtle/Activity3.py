import turtle
t = turtle.Screen()
t.bgcolor("black")
t.setup(400, 300)
t.title("Welcome to Turtle Window")
board = turtle.Turtle()
colors = ['red', 'blue', 'yellow', 'green']
board.speed(10)
board.hideturtle()
while True:
    for x in range(200):
     board.pencolor(colors[x%len(colors)])
     board.width(x//100 + 1)
     board.forward(x)
     board.left(59)
    board.right(239)
    for x in range(200, 0, -1):
     board.pencolor('black')
     board.width(x//100 + 7)
     board.forward(x)
     board.right(59)