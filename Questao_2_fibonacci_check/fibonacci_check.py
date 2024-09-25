def is_fibonacci_number(num):
    """
    Verifica se um número está na sequência de Fibonacci.

    Parâmetros:
    num (int): O número a ser verificado.

    Retorna:
    bool: True se o número estiver na sequência de Fibonacci, False caso contrário.
    """
    
    # Inicializa os dois primeiros números de Fibonacci
    a, b = 0, 1
    
    # Saída antecipada se o número for 0 ou 1
    if num == 0 or num == 1:
        return True
    
    # Gera números de Fibonacci até alcançar ou exceder o número alvo
    while b < num:
        a, b = b, a + b
    
    # Verifica se o número é igual ao número atual de Fibonacci
    return b == num

def main():
    # Entrada: Número a ser verificado
    number = int(input("Digite um número: "))
    
    # Verifica se o número está na sequência de Fibonacci
    if is_fibonacci_number(number):
        print(f"{number} está na sequência de Fibonacci.")
    else:
        print(f"{number} não está na sequência de Fibonacci.")

# Executa a função principal
if __name__ == "__main__":
    main()