#Calculadora do balacobaco

import sys
import matplotlib.pyplot as plt  # Importe a biblioteca matplotlib

a = int(input("Insira o valor da constante a "))
if a == 0:
    print("A constante a não pode ser igual a 0")
else:
    b = int(input("Insira o valor da constante b "))
    c = int(input("Insira o valor da constante c "))

    Delta = b**2 - 4*a*c

    x1 = (-b + (Delta)**(1/2)) / (2 * a)
    x2 = (-b - (Delta)**(1/2)) / (2 * a)

    Xv = (-b / (2 * a))
    Yv = (-Delta / (4 * a))

    if a > 0:
        print("A parábola será virada para cima")
    elif a < 0:
        print("A parábola será virada para baixo")
    print("Delta é = %.2f" % (Delta))
    print("O vértice é (%.2f, %.2f)" % (Xv, Yv))

    if Delta > 0:
        if Xv > x1:
            print("O ponto da esquerda é (%.2f, 0.00)" % (x1))
        elif Xv < x1:
            print("O ponto da direita é (%.2f, 0.00)" % (x1))
        if Xv > x2:
            print("O ponto da esquerda é (%.2f, 0.0)" % (x2))
        elif Xv < x2:
            print("O ponto da direita é (%.2f, 0.00)" % (x2))

    elif Delta <= 0:
        print("O ponto da esquerda é (0.00, %.2f)" % (c))

    # Criar um conjunto de pontos para plotar a parábola
    x = [x for x in range(int(Xv) - 10, int(Xv) + 11)]  # Gere valores de x
    y = [a * xi**2 + b * xi + c for xi in x]  # Calcule os valores correspondentes de y

    # Plotar a parábola
    plt.plot(x, y)
    plt.xlabel("Eixo X")
    plt.ylabel("Eixo Y")
    plt.title("Gráfico da Parábola")
    plt.grid(True)
    plt.show()  # Exibir o gráfico

