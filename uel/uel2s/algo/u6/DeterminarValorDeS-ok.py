## arquivo necessita de ajustes de indentação 
## ps: Esse já está ajustado.

def main():
    # Cria uma lista(vetor) com 0s (zero)
    A = [0 for _ in range(20)]
    for i in range(20):
        A[i] = int(input())

    j = 19
    S = 0
    for i in range(10):
        S = S + (A[i]-A[j])**2
        j = j - 1
    print(S)

if __name__ == "__main__":
    main()

