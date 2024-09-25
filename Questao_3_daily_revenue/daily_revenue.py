import json

def process_faturamento(file_path):
    """
    Processa o faturamento diário a partir de um arquivo JSON.

    Parâmetros:
    file_path (str): O caminho para o arquivo JSON com dados de faturamento.

    Retorna:
    tuple: Menor valor, maior valor, e número de dias com faturamento acima da média.
    """
    # Carrega os dados do arquivo JSON
    with open(file_path, 'r') as file:
        faturamento = json.load(file)

    # Filtra os dias com faturamento
    faturamento_filtrado = [dia['valor'] for dia in faturamento if dia['valor'] > 0]

    # Calcula o menor e maior valor de faturamento
    menor_valor = min(faturamento_filtrado)
    maior_valor = max(faturamento_filtrado)

    # Calcula a média mensal ignorando dias sem faturamento
    media_mensal = sum(faturamento_filtrado) / len(faturamento_filtrado)

    # Conta os dias com faturamento acima da média
    dias_acima_da_media = sum(1 for valor in faturamento_filtrado if valor > media_mensal)

    return menor_valor, maior_valor, dias_acima_da_media

def main():
    # Caminho para o arquivo JSON
    file_path = 'dados.json'

    # Processa os dados de faturamento
    menor_valor, maior_valor, dias_acima_da_media = process_faturamento(file_path)

    # Exibe os resultados
    print(f"Menor valor de faturamento: {menor_valor}")
    print(f"Maior valor de faturamento: {maior_valor}")
    print(f"Número de dias acima da média mensal: {dias_acima_da_media}")

# Executa a função principal
if __name__ == "__main__":
    main()