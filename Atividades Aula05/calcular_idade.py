from datetime import datetime

def calcular_idade_em_dias(data_nascimento_str):
  """
  Calcula a idade de uma pessoa em dias.

  Args:
    data_nascimento_str: A data de nascimento da pessoa no formato "dd/mm/aaaa".

  Returns:
    A idade da pessoa em dias (inteiro), ou None se o formato da data for inválido.
  """
  try:
    # Converte a string da data de nascimento para um objeto datetime
    data_nascimento = datetime.strptime(data_nascimento_str, "%d/%m/%Y")
    # Obtém a data atual
    data_atual = datetime.now()
    # Calcula a diferença entre as datas
    diferenca = data_atual - data_nascimento
    # Retorna a diferença em dias
    return diferenca.days
  except ValueError:
    print("Formato de data inválido. Use dd/mm/aaaa.")
    return None

# Solicita a data de nascimento ao usuário
data_nascimento_input = input("Digite sua data de nascimento (dd/mm/aaaa): ")

# Calcula a idade em dias
idade_dias = calcular_idade_em_dias(data_nascimento_input)

# Exibe o resultado
if idade_dias is not None:
  print(f"Você tem {idade_dias} dias de vida.")