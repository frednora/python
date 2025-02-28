# Unidade 5, Atividade 1.
# Aluno: Frederico Martins Nora.

# Descrição da atividade:
# Faça um programa em Python que leia a dimensão de 3 lados de um triângulo. 
# + O programa deverá informar se os valores podem ser um triângulo. 
# + Indique, caso os lados formem um triângulo, se o mesmo é: 
# equilátero, isósceles ou escaleno.

# Os tipo de triângulos usados.
# Triângulo Equilátero: Três lados iguais;
# Triângulo Isósceles:  Quaisquer dois lados iguais;
# Triângulo Escaleno:   Três lados diferentes;

# Função para verificar se os três lados realmente formam um triângulo.
# Três lados formam um triângulo quando 
# a soma de quaisquer dois lados for maior que o terceiro.
def eh_triangulo(lado1, lado2, lado3):
    if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
        return True
    else:
        return False

# Função para determinar o tipo de triângulo
def tipo_triangulo(lado1, lado2, lado3):
    if lado1 == lado2 == lado3:
        return "Equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        return "Isósceles"
    else:
        return "Escaleno"

# Função principal.
def main():

    print("Atividade 1:")
    print("Vamos analisar um triangulo.")
    print("Primeiro informe os valores dos lados do triângulo!")

    # Solicitar ao usuário para inserir os três lados
    lado1 = float(input("Digite o comprimento do primeiro lado: "))
    lado2 = float(input("Digite o comprimento do segundo lado: "))
    lado3 = float(input("Digite o comprimento do terceiro lado: "))

    # Verificar se os lados formam um triângulo e determinar o tipo
    if eh_triangulo(lado1, lado2, lado3):
        print("Os valores formam um triângulo", tipo_triangulo(lado1, lado2, lado3))
    else:
        print("Os valores não formam um triângulo")

# Rotina de inicializaão do programa.
if __name__ == "__main__":
    main()

