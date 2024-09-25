def calcular_percentuais(faturamento):
    """
    Calcula o percentual de representação de cada estado.

    Parâmetros:
    faturamento (dict): Dicionário com o faturamento de cada estado.

    Retorna:
    dict: Percentuais de cada estado.
    """
    total = sum(faturamento.values())
    percentuais = {estado: (valor / total) * 100 for estado, valor in faturamento.items()}
    return percentuais

def main():
    # Faturamento mensal por estado
    faturamento = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53
    }
    
    # Calcula os percentuais
    percentuais = calcular_percentuais(faturamento)
    
    # Exibe os resultados
    for estado, percentual in percentuais.items():
        print(f"{estado}: {percentual:.2f}%")

# Executa a função principal
if __name__ == "__main__":
    main()