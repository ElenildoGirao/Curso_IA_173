import re

def eh_palindromo(texto):
  """
  Verifica se um texto é um palíndromo.

  Um palíndromo é uma palavra, frase, número ou outra sequência de caracteres
  que lê o mesmo para trás e para a frente, como "madam" ou "ana".

  Args:
    texto: A string a ser verificada.

  Returns:
    True se o texto for um palíndromo, False caso contrário.
  """
  # 1. Normalizar o texto:
  #    - Converter para minúsculas para ignorar diferenças de caixa (maiúsculas/minúsculas).
  #    - Remover espaços, pontuações e acentos para focar apenas nos caracteres alfanuméricos.
  texto_normalizado = texto.lower()
  # Remover pontuações e espaços usando expressões regulares
  # Esta expressão regular mantém apenas letras e números
  texto_normalizado = re.sub(r'[^a-z0-9]', '', texto_normalizado)


  # 2. Verificar se o texto normalizado é igual ao seu inverso
  if not texto_normalizado: # String vazia pode ou não ser considerada palíndromo, aqui consideramos que não.
      return False
  return texto_normalizado == texto_normalizado[::-1]

# Exemplos de uso:
texto_usuario = input("Digite uma palavra ou frase para verificar se é um palíndromo: ")

if eh_palindromo(texto_usuario):
  print(f"'{texto_usuario}' é um palíndromo!")
else:
  print(f"'{texto_usuario}' não é um palíndromo.")
