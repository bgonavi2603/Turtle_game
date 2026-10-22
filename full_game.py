"""Primer hito: carrera de dos tortugas.

La infraestructura gráfica ya está resuelta. Los TODO sólo requieren variables,
condicionales y bucles, que son los contenidos impartidos al anunciar M1.
"""

from __future__ import annotations

import turtle


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
START_X = -320
FINISH_X = 300

# TODO 1: asigna dos velocidades positivas. Predice quién ganará.
RED_SPEED = 1
BLUE_SPEED = 1
#Aqui elejimos estas velocidades.
#Este condicional permite que el usuario elija una velocidad que no se corresponda a un numero. Aunque en este caso no cambia el codigo porque en el siguiente condicional esta pensado para que haga una comparación booleana de numeros enteros, no con una cadena de caracteres.
#Como la velocidad de la tortuga roja es mayor que la de la azul va a ganar la roja.

def prepare_game():
    """Prepara la ventana, la pista y las dos tortugas (código proporcionado)."""
    screen = turtle.Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.title("Carrera de tortugas")

    painter = turtle.Turtle(visible=False)
    painter.speed(0)
    for y in (-80, 0, 80):
        painter.penup()
        painter.goto(START_X, y)
        painter.pendown()
        painter.forward(FINISH_X - START_X)

    red = turtle.Turtle(shape="turtle")
    red.color("red")
    red.penup()
    red.goto(START_X, 40)

    blue = turtle.Turtle(shape="turtle")
    blue.color("blue")
    blue.penup()
    blue.goto(START_X, -40)
    return screen, red, blue


def run_race(red, blue):
    """Mueve las tortugas hasta que una alcance la meta."""
    # TODO 2: valida con un condicional que ambas velocidades sean positivas.
    # Si alguna no lo es, muestra un mensaje y devuelve una cadena vacía.
    if RED_SPEED <= 0:
        print("Error: La velocidad de la tortuga roja debe ser positiva.")
        return ""
    if BLUE_SPEED <= 0:
        print("Error: La velocidad de la tortuga azul debe ser positiva.")
        return ""
#Sin este if el usuario puede poner la velocidad que quiera, lo cual puede no tener sentido porque una velocidad siempre va a ser >=0.

    # TODO 3: crea un bucle que mueva las dos tortugas en cada vuelta.
    # Cuando una alcance FINISH_X, devuelve "roja" o "azul".
    # Si las dos alcanzan FINISH_X en la misma vuelta, devuelve "empate".
    while True:
        red.fd(RED_SPEED)
        blue.fd(BLUE_SPEED)
        #Con la función fordard (fd) hacemos que las tortugas se muevan hacia adelante según la velocidad que le asignamos a cada una.

        posicion_red = red.xcor()
        posicion_blue = blue.xcor()
        #Con la función xcor obtenemos la posición en el eje x de cada tortuga.

        if posicion_red >= FINISH_X and posicion_blue >= FINISH_X:
            return "empate"
        elif posicion_red >= FINISH_X:
            return "roja"
        elif posicion_blue >= FINISH_X:
            return "azul"
        #Este if nos permite controlar cuando llegan las tortugas a la meta y cual de las dos es la ganadora o si hay empate.
#Usamos un while true para que el bucle se ejecute indefinidamente hasta que una de las tortugas llegue a la meta.

def main():
    """Pone en marcha la carrera (código proporcionado)."""
    screen, red, blue = prepare_game()
    winner = run_race(red, blue)
    if winner == "empate":
        screen.title("¡Empate! Las dos tortugas llegan a la vez")
    elif winner:
        screen.title(f"¡Ha ganado la tortuga {winner}!")
    screen.mainloop()


if __name__ == "__main__":
    main()

#Si las dos velocidades son positivas, la tortuga con mayor velocidad ganará.
#Si las dos velocidades son iguales, habrá un empate.
#Si alguna de las velocidades es negativa, se mostrará un mensaje de error y no se ejecutará la carrera.
#El resultado del caso anterior se repetirá si alguna de las velocidades es 0 porque en el condicional se imponen que sean mayores a 0.