# Atividade 2 da Unidade 6.
# Aluno: Frederico Martins Nora.

# Escreva um programa em Python que leia o conteúdo de uma matriz A, 
# com dimensão 2x3 e calcule a matriz transposta AT. 
# Na matriz transposta, a linha i se torna a coluna i. 
# Escrever a matriz transposta.

'''
Exemplo:
A=  |1 2 3|
    |4 5 6|
Matriz transposta será:
    |1 4|
AT= |2 5|
    |3 6|
'''

# Função principal.
def main():

    # Banner
    print ("Atividade 2: Encontrar a matriz transposta de uma dada matriz")

    # Matriz A, 2x3.
    A = [
        [0,0,0],
        [0,0,0]
    ]

    # Matriz transposta AT, 3x2.
    AT = [
        [0,0],
        [0,0],
        [0,0]
    ]

    # ======================================
    # Obter os valores da matriz original 2x3.

    # Vamos pegar os valores para a primeira linha
    print ("Digite três valores para a primeira linha de nossa matriz")
    for i in range(3):
        A[0][i] = int( input() )

    # Vamos pegar os valores para a segunda linha
    print ("Digite três valores para a segunda linha de nossa matriz")
    for i in range(3):
        A[1][i] = int( input() )

    # ======================================
    # Vamos cria a matriz transposta 3x2 com base na matriz original 2x3.

    # Os valores da primeira linha da matriz original passam a a ser 
    # os valores da primeira coluna da matriz transposta.
    for i in range(3):
        AT[i][0] = A[0][i]

    # Os valores da segunda linha da matriz original passam a a ser 
    # os valores da segunda coluna da matriz transposta.
    for i in range(3):
        AT[i][1] = A[1][i] 

    # Imprimir a matriz transposta.
    print ("Essa é a matriz transposta")
    print(AT)

# Rotina de inicialização.
if __name__ == "__main__":
    main()

