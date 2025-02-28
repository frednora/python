# Atividade 1 da Unidade 6.
# Aluno: Frederico Martins Nora.

# Faça um programa em Python (contendo uma função) que 
# + leia o conteúdo de um vetor de 5 elementos, em seguida 
# + leia o valor de N, rotacionando o vetor N posições para a direita. 
# A função deve receber o vetor e o número de rotações como entrada. 
# O programa deve encerrar quando inserir o valor 0 (zero) para N. 
# Imprimir o vetor resultante para cada rotação.
# Exemplo:
# Para o vetor [1, 2, 3, 4, 5] e N=2 rotações, o resultado deve ser: [4, 5, 1, 2, 3].

# Realiza a rotação dos valores dentro de uma dada lista.
# INPUT:
#   target_list = A lista onde iremos fazer a rotação.
#   num = Número de rotações
# OUTPUT:
#   Nova lista
def rotacao_para_direita(target_list, num):

    # Número inválido de rotações.
    if num == 0:
        return target_list

    # Nova lista
    output_list = []
    # Posição na lista antiga de onde começaremos a nova lista.
    StartPosition = len(target_list) - num
    # O comprimento da lista antiga.
    ListLength = len(target_list)

    # Vamos adicionar valores na nova lista,
    # copiando da antiga a partir do índice inicial,
    # que equivale ao valor da rotação.  
    for item in range( StartPosition, ListLength ):
        output_list.append(target_list[item])
 
    # Vamos copiar os ítens que faltaram.
    # Eles estão antes do indice que equivale ao
    # valor da rotação.
    # Isso finaliza nossa nova lista.
    for item in range(0, StartPosition):
        output_list.append(target_list[item])
 
    # Vamos retornar a nossa nova lista
    # já feita a rotação dos ítens.
    return output_list
 

# Função principal.
def main():
    # Banner
    print("Atividade 1: Rotação de lista.")

    # Vamos criar nosso vetor.
    print("==== #### ====")
    print("Digite os valores para um lista com 5 elementos!")
    MyList = [0 for _ in range(5)]
    # Vamos pegar os valores
    for i in range(5):
        MyList[i] = int( input() )

# Loop
# Agora que já temos os valores para os ítens de nossa lista,
# então vamos rotacionar os ítems da lista conforme desejado pelo usuário.
# Faremos isso várias vezes. Mas quando o valor da rotação for igua a zero, 
# então devemos encerrar o programa.

    while True:
        # Número de rotações
        print("Digite o número de rotações desejadas!")
        N=0
        N = int( input() )
        if N == 0:
            print("[Zero rotações]: Fim do programa")
            return
        # Cria um lista vazia.
        FinalList = []
        # Chama a função que vai fazer a rotação.
        FinalList = rotacao_para_direita(MyList,N)
        # Imprime a lista já feita a rotação.
        print(FinalList)
        # Atualize a lista de entrada, para que seja a lista mais atual.
        MyList = FinalList
        print("Fim da etapa")

# Rotina de inicialização.
if __name__ == "__main__":
    main()

