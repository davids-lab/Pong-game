from turtle import Turtle,Screen
from pad_derecho import Pad
from pelota import  Pelota
from puntaje import Puntaje
import time

pantalla = Screen()
pantalla.setup(width=800, height=600)
pantalla.bgcolor("black")
pantalla.title("David's PONG")
pantalla.listen()
pantalla.tracer(0)

pad_derecho = Pad(350,0)
pad_izquierdo = Pad(-350,0)

pelota = Pelota()
puntaje = Puntaje()


pantalla.onkeypress(pad_derecho.mover_arriba, "Up")
pantalla.onkeypress(pad_derecho.mover_abajo, "Down")
pantalla.onkeypress(pad_izquierdo.mover_arriba, "w")
pantalla.onkeypress(pad_izquierdo.mover_abajo, "s")


juego_encendido = True


while juego_encendido:
    time.sleep(pelota.velocidad)
    pantalla.update()
    pelota.movimiento()

    #Detectar impacto con la pelota
    if pelota.ycor() >= 280 or pelota.ycor() <= -280:
        pelota.rebotar_y()

    #Detectar impacto con los pad
    if pelota.distance(pad_derecho) < 50 and pelota.xcor() > 330 or pelota.distance(pad_izquierdo) < 50 and pelota.xcor() < -330:
        pelota.rebotar_x()

    #Detectar pelota haciendo gol derecha
    if pelota.xcor() > 380:
        pelota.resetear_posicion()
        puntaje.punto_izquierdo()

    # Detectar pelota haciendo gol izquierda
    if pelota.xcor() < -380:
        pelota.resetear_posicion()
        puntaje.punto_derecho()








pantalla.exitonclick()
