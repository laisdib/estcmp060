# Programa em Pyhton para fazer triângulos usando o Turtle
import turtle


# Método Scree() para obter a tela
tela = turtle.Screen()

# Criando a caneta
caneta = turtle.Turtle()


def triangulo(x, y):
    # Movimento a caneta para o local clicado pelo usuário
    # na coordenada (x, y)
    caneta.penup()
    caneta.goto(x, y)
    caneta.pendown()

    for i in range(3):
        # Move o cursor por 100 pixels e virando-a 120 graus à esquerda
        caneta.forward(100)
        caneta.left(120)
        caneta.forward(100)


# Identificando o click e a posição clicada
turtle.onscreenclick(triangulo, 1)
turtle.listen()

# Pausando
turtle.done()
