from turtle import Turtle
import time

class Pelota(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_var = 10
        self.y_var = 10
        self.velocidad = 0.1

    def movimiento(self):
        new_x = self.xcor() + self.x_var
        new_y = self.ycor() + self.y_var
        self.goto(new_x, new_y)

    def rebotar_y(self):
        self.y_var *= -1

    def rebotar_x(self):
        self.x_var *= -1
        self.velocidad *= 0.9

    def resetear_posicion(self):
        self.home()
        self.x_var *= -1
        self.velocidad = 0.1