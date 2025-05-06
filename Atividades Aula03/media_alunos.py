def registrar_medias_alunos():
    """
    Registra nomes de alunos, suas notas, calcula a média e exibe os resultados.
    """
    alunos = {}  # Usaremos um dicionário para armazenar os dados dos alunos
    continuar_registro = True

    print("--- Sistema de Registro de Médias dos Alunos ---")

    while continuar_registro:
        nome_aluno = input("\nDigite o nome do aluno (ou 'sair' para finalizar): ")
        if nome_aluno.lower() == 'sair':
            continuar_registro = False
            break

        notas_aluno = []
        numero_de_notas = 0
        while True:
            try:
                numero_de_notas = int(input(f"Quantas notas você deseja registrar para {nome_aluno}? "))
                if numero_de_notas > 0:
                    break
                else:
                    print("Por favor, insira um número de notas maior que zero.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número inteiro.")

        print(f"--- Insira as {numero_de_notas} notas para {nome_aluno} ---")
        for i in range(numero_de_notas):
            while True:
                try:
                    nota_str = input(f"Digite a nota {i + 1}: ").replace(',', '.') # Permite vírgula como separador decimal
                    nota = float(nota_str)
                    if 0 <= nota <= 10: # Assumindo que as notas são de 0 a 10
                        notas_aluno.append(nota)
                        break
                    else:
                        print("Nota inválida. Por favor, insira um valor entre 0 e 10.")
                except ValueError:
                    print("Entrada inválida. Por favor, insira um número para a nota.")

        if notas_aluno: # Calcula a média apenas se houver notas
            media = sum(notas_aluno) / len(notas_aluno)
            alunos[nome_aluno] = {'notas': notas_aluno, 'media': media}
            print(f"Média de {nome_aluno} registrada: {media:.2f}")
        else:
            print(f"Nenhuma nota registrada para {nome_aluno}.")

    # Exibir resultados
    if alunos:
        print("\n--- Médias Finais dos Alunos ---")
        for nome, dados in alunos.items():
            print(f"Aluno: {nome}")
            print(f"  Notas: {', '.join(map(str, dados['notas']))}") # Exibe as notas formatadas
            print(f"  Média: {dados['media']:.2f}")
            # Você pode adicionar um status de aprovação/reprovação aqui
            if dados['media'] >= 7.0: # Exemplo de critério de aprovação
                print("  Status: Aprovado")
            elif dados['media'] >= 5.0:
                print("  Status: Recuperação")
            else:
                print("  Status: Reprovado")
            print("-" * 20)
    else:
        print("\nNenhum aluno foi registrado.")

    print("--- Fim do Sistema ---")

# Executa o sistema de registro
if __name__ == "__main__":
    registrar_medias_alunos()