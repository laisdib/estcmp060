# Programa em Python para traçar
# a espiral fractal de Fibonacci usando Turtle
import turtle
import math


def tracando_fib(iteracoes):
    fibonacci_0 = 0
    fibonacci_1 = 1
    quadrado_0 = fibonacci_0
    quadrado_1 = fibonacci_1

    # Definindo a cor da caneta para preto
    caneta.pencolor("black")

    # Desenhando o primeiro quadrado
    caneta.forward(fibonacci_1 * fator_mult)
    caneta.left(90)

    caneta.forward(fibonacci_1 * fator_mult)
    caneta.left(90)

    caneta.forward(fibonacci_1 * fator_mult)
    caneta.left(90)

    caneta.forward(fibonacci_1 * fator_mult)

    # Executando Fibonacci
    aux = quadrado_1
    quadrado_1 += quadrado_0
    quadrado_0 = aux

    # Desenhando o resto dos quadrados
    for i in range(1, iteracoes):
        caneta.backward(quadrado_0 * fator_mult)
        caneta.right(90)

        caneta.forward(quadrado_1 * fator_mult)
        caneta.left(90)

        caneta.forward(quadrado_1 * fator_mult)
        caneta.left(90)

        caneta.forward(quadrado_1 * fator_mult)

        # Executando Fibonacci
        aux = quadrado_1
        quadrado_1 += quadrado_0
        quadrado_0 = aux

    # Trazendo a caneta para o ponto inicial do espiral
    caneta.penup()
    caneta.setposition(fator_mult, 0)
    caneta.seth(0)
    caneta.pendown()

    # Definindo a cor da caneta para vermelho
    caneta.pencolor("red")

    # Gráfico - espiral Fibonacci
    caneta.left(90)
    for i in range(iteracoes):
        print(fibonacci_1)
        tragetoria = (math.pi*fibonacci_1*fator_mult) / 2
        tragetoria /= 90

        for j in range(90):
            caneta.forward(tragetoria)
            caneta.left(1)

        aux = fibonacci_0
        fibonacci_0 = fibonacci_1
        fibonacci_1 += aux


# Lendo valor de iterações que o código irá rodar inserido pelo usuário
iteracoes = int(input("Insira o número de iterações (deve ser > 1): "))

# 'Fator_mult' significa o fator multiplicativo que aumenta ou diminui
# a escala de formação do gráfico por um fator expecífico
fator_mult = int(input("Insira a escala do gráfico: (deve ser >= 1): "))

# Plotando o Gráfico de Fibonacci em espiral e imprimindo
# na tela o número de Fibonacci correspondente
if iteracoes > 1:
    print("Série de Fibonacci de", iteracoes, "elementos: ")
    caneta = turtle.Turtle()
    caneta.speed(100)
    tracando_fib(iteracoes)
    turtle.done()
else:
    print("O número de iterações precisa ser > 1")
