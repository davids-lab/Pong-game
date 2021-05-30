from turtle import Turtle

class Pad(Turtle):
    def __init__(self, x_coord, y_coord):
        super().__init__()
        self.penup()
        self.goto(x=x_coord, y=y_coord)
        self.shape("square")
        self.color("white")
        self.turtlesize(5.0,1.0)


    def mover_arriba(self):
        if self.ycor() < 240:
            nuevo_y = self.ycor() + 20
            self.goto(self.xcor(), nuevo_y)

    def mover_abajo(self):
        if self.ycor() > -240:
            nuevo_y = self.ycor() - 20
            self.goto(self.xcor(), nuevo_y)

