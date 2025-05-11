def calcular_gorjeta(total_conta, porcentagem_gorjeta):
    """
    Calcula o valor da gorjeta e o total da conta com a gorjeta.

    Args:
        total_conta (float): O valor total da conta.
        porcentagem_gorjeta (float): A porcentagem da gorjeta desejada (ex: 15 para 15%).

    Returns:
        tuple: Uma tupla contendo o valor da gorjeta e o valor total da conta com a gorjeta.
               (valor_da_gorjeta, total_com_gorjeta)
               Retorna (None, None) se a entrada for inválida.
    """
    if total_conta < 0 or porcentagem_gorjeta < 0:
        print("Erro: O total da conta e a porcentagem da gorjeta não podem ser negativos.")
        return None, None
    
    valor_da_gorjeta = total_conta * (porcentagem_gorjeta / 100)
    total_com_gorjeta = total_conta + valor_da_gorjeta
    return valor_da_gorjeta, total_com_gorjeta

# Exemplo de uso:
if __name__ == "__main__":
    print("Calculadora de Gorjeta")
    print("-" * 20)

    try:
        # Solicita ao usuário o total da conta
        entrada_total_conta = input("Digite o valor total da conta: R$ ")
        # Remove vírgulas e converte para ponto flutuante, se necessário
        total_conta = float(entrada_total_conta.replace(',', '.'))

        # Solicita ao usuário a porcentagem da gorjeta
        entrada_porcentagem = input("Digite a porcentagem da gorjeta que você gostaria de dar (ex: 10, 15, 20): ")
        porcentagem_gorjeta = float(entrada_porcentagem.replace(',', '.'))

        # Calcula a gorjeta
        valor_gorjeta_calculado, total_final_com_gorjeta = calcular_gorjeta(total_conta, porcentagem_gorjeta)

        if valor_gorjeta_calculado is not None:
            # Exibe os resultados formatados como moeda brasileira
            print("\n--- Recibo ---")
            print(f"Total da conta: R$ {total_conta:.2f}")
            print(f"Porcentagem da gorjeta: {porcentagem_gorjeta:.1f}%")
            print(f"Valor da gorjeta: R$ {valor_gorjeta_calculado:.2f}")
            print(f"Total com gorjeta: R$ {total_final_com_gorjeta:.2f}")
            print("--------------")

    except ValueError:
        print("\nErro: Entrada inválida. Por favor, certifique-se de digitar números válidos para o total da conta e a porcentagem.")
    except Exception as e:
        print(f"\nOcorreu um erro inesperado: {e}")