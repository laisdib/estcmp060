import turtle


# Função para traçar o 'Y'
def tracando_y(tamanho, nivel):

    if nivel > 0:
        # Alterando o modo de cor para RGB
        turtle.colormode(255)

        # Dividindo o intervalo RGB para verde em intervalos iguais
        # para cada nível
        # Definindo a cor conforme o nível atual
        pen.pencolor(0, 255//nivel, 0)

        # Desenhando a base
        pen.forward(tamanho)
        pen.right(angulo)

        # Criando os galhos da árvore
        tracando_y(0.8*tamanho, nivel-1)
        pen.pencolor(0, 255//nivel, 0)

        # Girando a tartaruga para a esquerda
        pen.left(2 * angulo)
        tracando_y(0.8*tamanho, nivel-1)

        pen.pencolor(0, 255//nivel, 0)
        pen.right(angulo)
        pen.forward(-tamanho)


# Criando a caneta, definindo a velocidade e virando-a para cima
pen = turtle.Turtle()
pen.speed('fastest')
pen.right(-90)

# Definindo o ângulo entre a base e os ramos do 'Y'
angulo = 30

# Árvore de tamanho 80 e nível 15
tracando_y(80, 15)

# Para a tela não fechar ao final da execução do programa
turtle.done()