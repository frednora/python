# Execício nos slides da Unidade 6.

def main():
    N = int( input("Entre com o valor de N: ") )
    fatorial = 1
    if N > 1:
        for i in range(2, N+1):
            fatorial = fatorial * i 
    print (f"Fatorial de (N) = {fatorial}")

if __name__ == "__main__":
    main()

