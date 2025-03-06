# Exercício Unidade 3.

# A conversão de graus Farenheit para centígrados é obtida por C = 5/9 * (F – 32). 
# Faça um algoritmo que calcule e escreva uma tabela de centígrados em função de graus Farenheit, que
# variam de 50 a 60 de 1 em 1.

def main():
    # Optional: Print a header for the table
    print("Fahrenheit to Celsius Table")
    print("Fahrenheit | Celsius")
    print("-----------|--------")
    
    # Loop from 50 to 60 inclusive
    for i in range(50, 61):
        C_Value = (5/9) * (i - 32)
        # Format output with 2 decimal places for readability
        print(f"{i} F       | {C_Value:.2f} C")

if __name__ == "__main__":
    main()
