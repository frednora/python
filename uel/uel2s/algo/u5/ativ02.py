# Unidade 5, Atividade 2.
# Aluno: Frederico Martins Nora.

# Descrição da atividade:
# Faça um programa que calcule 
# + as raízes de uma equação do segundo grau, na forma ax² + bx + c. 
# O programa deverá ler os valores de a, b e c e fazer as consistências, 
# informando ao usuário nas seguintes situações:
# + Se o usuário informar o valor de A igual a zero, 
#  a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
# + Se o delta calculado for negativo, 
#  a equação não possui raízes reais. Informe ao usuário e encerre o programa;
# + Se o delta calculado for igual a zero 
#  a equação possui apenas uma raiz real; informe-a ao usuário;
# + Se o delta for positivo, 
#  a equação possui duas raiz reais; informe-as ao usuário;

import math

# Função para calcular as raízes da equação do segundo grau
# INPUT:
# Para uma equação do segundo grau, na forma ax² + bx + c, vamos precisar 
# de três parâmetros de entrada. (a,b e c).
def calcular_raizes(a, b, c):
    # Verificar se é uma equação do segundo grau.
    # Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e 
    # o programa não deve fazer pedir os demais valores, sendo encerrado.
    if a == 0:
        print("A equação não é do segundo grau.")
        return
    
    # Calcular o delta (discriminante)
    delta = b**2 - 4*a*c
    
    # Verificar se o delta é negativo
    # + Se o delta calculado for negativo, 
    #  a equação não possui raízes reais. Informe ao usuário e encerre o programa;
    # + Se o delta calculado for igual a zero 
    #  a equação possui apenas uma raiz real; informe-a ao usuário;
    # + Se o delta for positivo, 
    #  a equação possui duas raiz reais; informe-as ao usuário;

    if delta < 0:
        # Delta negativo. A equação não possue raizes reais.
        print("[Delta negativo]: A equação não possui raízes reais.")
        return
    elif delta == 0:
        # Delta igual a zero. A equação possui apenas uma raiz real.
        # Vamos calcular a raiz e imprimir o valor dela.
        # Lembrando da formula de Bhaskara, teremos nesse caso, 
        # (-b+0) ou (-b-0), que fica apenas -b no numerador.
        # Não precisa fazer a raiz de 0. math.sqrt(0).
        raiz = -b / (2*a)
        print(f"[Delta igual a zero]: A equação possui uma única raiz real: {raiz}")
    else:
        # O delta é positivo, a equação possui duas raiz reais
        # Calcular as duas raizes reais e imprimir.
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"[Delta positivo]: A equação possui duas raízes reais: R1={raiz1} e R2={raiz2}")


# Função principal.
def main():

    # Banner.
    print("Atividade 2:")
    print("Vamos encontrar as raízes de uma equação do segundo grau.")
    print("Primeiro informe alguns parâmetros para a equação!")

    # Pegar input do usuário.
    # Solicitar ao usuário para inserir os valores de a, b e c

    # Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e 
    # o programa não deve fazer pedir os demais valores, sendo encerrado.
    a = float(input("Digite o valor de a: "))
    if a == 0:
        print("A equação não é do segundo grau.")
        return

    b = float(input("Digite o valor de b: "))
    
    c = float(input("Digite o valor de c: "))

    # Calcular as raízes da equação
    # Os parâmetros da função são os valores digitados pelo usuário.
    calcular_raizes(a, b, c)

# Rotina de inicializaão do programa.
if __name__ == "__main__":
    main()
