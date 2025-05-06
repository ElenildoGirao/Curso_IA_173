def calculadora():
    """
    Uma calculadora simples que realiza operações de adição, subtração,
    multiplicação e divisão.
    """

    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    while True:
        # Solicita a escolha do usuário
        escolha = input("Digite sua escolha (1/2/3/4): ")

        # Verifica se a escolha é uma das opções válidas
        if escolha in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Entrada inválida. Por favor, insira números.")
                continue

            if escolha == '1':
                print(f"{num1} + {num2} = {adicao(num1, num2)}")

            elif escolha == '2':
                print(f"{num1} - {num2} = {subtracao(num1, num2)}")

            elif escolha == '3':
                print(f"{num1} * {num2} = {multiplicacao(num1, num2)}")

            elif escolha == '4':
                resultado_divisao = divisao(num1, num2)
                if isinstance(resultado_divisao, str): # Verifica se houve erro na divisão
                    print(resultado_divisao)
                else:
                    print(f"{num1} / {num2} = {resultado_divisao}")

            # Pergunta se o usuário quer fazer outro cálculo
            proximo_calculo = input("Deseja realizar outro cálculo? (sim/não): ")
            if proximo_calculo.lower() != 'sim':
                break
        else:
            print("Opção inválida.")

def adicao(x, y):
    """Esta função soma dois números"""
    return x + y

def subtracao(x, y):
    """Esta função subtrai dois números"""
    return x - y

def multiplicacao(x, y):
    """Esta função multiplica dois números"""
    return x * y

def divisao(x, y):
    """Esta função divide dois números"""
    if y == 0:
        return "Erro! Divisão por zero."
    else:
        return x / y

# Executa a calculadora
if __name__ == "__main__":
    calculadora()