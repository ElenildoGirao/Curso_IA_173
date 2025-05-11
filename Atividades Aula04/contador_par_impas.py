def contar_pares_impares(numeros):
    """
    Conta a quantidade de números pares e ímpares em uma lista.

    Args:
        numeros: Uma lista de números inteiros.

    Returns:
        Uma tupla contendo a contagem de números pares e ímpares, respectivamente.
        (pares, impares)
    """
    pares = 0
    impares = 0
    for numero in numeros:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares

# Exemplo de uso:
if __name__ == "__main__":
    try:
        # Solicita ao usuário para inserir números separados por espaço
        entrada_usuario = input("Digite uma lista de números inteiros separados por espaço: ")
        
        # Converte a entrada do usuário (string) em uma lista de inteiros
        lista_de_numeros = [int(item) for item in entrada_usuario.split()]
        
        # Chama a função para contar os números pares e ímpares
        quantidade_pares, quantidade_impares = contar_pares_impares(lista_de_numeros)
        
        # Exibe os resultados
        print(f"\nNa lista fornecida:")
        print(f"Quantidade de números pares: {quantidade_pares}")
        print(f"Quantidade de números ímpares: {quantidade_impares}")

    except ValueError:
        print("Entrada inválida. Por favor, certifique-se de digitar apenas números inteiros separados por espaço.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")