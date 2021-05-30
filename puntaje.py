from turtle import Turtle

class Puntaje(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.puntaje_izquierdo = 0
        self.puntaje_derecho = 0
        self.actualizar_puntaje()

    def actualizar_puntaje(self):
        self.goto(-100, 200)
        self.write(self.puntaje_izquierdo, align="center", font=("Courier", 50, "normal"))
        self.goto(100, 200)
        self.write(self.puntaje_derecho, align="center", font=("Courier", 50, "normal"))

    def punto_izquierdo(self):
        self.puntaje_izquierdo += 1
        self.clear()
        self.actualizar_puntaje()

    def punto_derecho(self):
        self.puntaje_derecho += 1
        self.clear()
        self.actualizar_puntaje()
