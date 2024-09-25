# Função que inverte os caracteres de uma string
def inverter_string(s):
    """
    Esta função recebe uma string como argumento e retorna
    a string com os caracteres invertidos.
    
    Parâmetros:
    s (str): A string que será invertida.
    
    Retorna:
    str: A string invertida.
    """
    # Inicializa uma string vazia para armazenar o resultado
    string_invertida = ""
    
    # Percorre a string original do último caractere até o primeiro
    for i in range(len(s) - 1, -1, -1):
        # Adiciona o caractere atual à string invertida
        string_invertida += s[i]
    
    return string_invertida

# Entrada da string (pode ser alterada para qualquer string desejada)
string_original = input("Digite a string que você deseja inverter: ")

# Chama a função e armazena o resultado
resultado = inverter_string(string_original)

# Exibe o resultado
print("String invertida:", resultado)
