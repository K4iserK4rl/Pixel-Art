from turtle import Turtle, Screen

screen = Screen()

t = Turtle()
tSize = 20
t.hideturtle()
t.speed(0)

t.penup()
t.goto(tSize / 2 - screen.window_width() / 2, screen.window_height() / 2 - tSize / 2)
t.pendown()

side = 30

pixelList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
           #Black     #Purple    #White     #Hot Pink  #Gray      #Light Purple 
colors = ["#000000", "#ba27d6", "#ffffff", "#f40bdd", "#9f9d9f", "#e0bee8",
           #Lighter Purple  #Dark Purple  #Dark Pink  #Darker Purple
          "#f3e5f6",       "#ac2bc4",    "#bf31b1",  "#97248c"]

grid = [
        [2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2],
        [2, 2, 2, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 2, 2, 2],
        [2, 2, 0, 3, 3, 3, 1, 1, 1, 1, 1, 3, 3, 3, 8, 0, 2, 2],
        [2, 0, 2, 3, 3, 3, 7, 7, 1, 1, 3, 2, 2, 3, 3, 8, 0, 2],
        [2, 9, 3, 3, 3, 1, 7, 7, 1, 1, 3, 2, 2, 3, 3, 8, 0, 2],
        [0, 3, 3, 3, 8, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 8, 8, 2],
        [0, 3, 3, 8, 1, 6, 1, 6, 1, 1, 1, 3, 3, 3, 3, 8, 8, 0],
        [0, 8, 8, 1, 6, 1, 6, 1, 6, 1, 1, 1, 3, 3, 8, 8, 8, 0],
        [0, 9, 1, 1, 6, 1, 6, 1, 6, 1, 1, 1, 9, 8, 8, 8, 9, 0],
        [0, 9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9, 9, 9, 9, 9, 0],
        [0, 0, 9, 1, 1, 0, 0, 0, 1, 1, 9, 9, 9, 9, 9, 9, 0, 0],
        [0, 0, 0, 0, 0, 6, 2, 6, 0, 9, 9, 9, 9, 0, 0, 0, 0, 0],
        [2, 0, 4, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 4, 0, 2],
        [2, 0, 6, 2, 0, 6, 2, 6, 0, 0, 0, 0, 0, 4, 6, 5, 0, 2],
        [2, 2, 0, 6, 2, 0, 0, 0, 6, 6, 6, 6, 6, 6, 5, 0, 2, 2],
        [2, 2, 2, 0, 5, 6, 6, 6, 6, 6, 6, 6, 5, 5, 0, 2, 2, 2],
        [2, 2, 2, 2, 0, 0, 5, 5, 5, 5, 5, 5, 0, 0, 2, 2, 2, 2],
        [2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2]
       ]

numCol = len(grid[0])

def square(color):
    t.color(color)
    t.begin_fill()
    for num in range(4):
        t.fd(side)
        t.rt(90)
    t.end_fill()
    t.fd(side)

def newRow():
    t.down()
    t.right(90)
    t.fd(side)
    t.right(90)
    t.fd(numCol * side)
    t.rt(180)
    t.up()

for pixel in grid:
    for num in pixel:
        square(colors[num])
    newRow()

screen.mainloop()
