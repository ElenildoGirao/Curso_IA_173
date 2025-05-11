import re # Módulo para expressões regulares, útil para verificações

def verificar_forca_senha_numeros_letras(senha):

    mensagens_erro = []
    
    # Critério 1: Comprimento mínimo de 8 caracteres
    if len(senha) < 8:
        mensagens_erro.append("A senha deve ter no mínimo 8 caracteres.")

    # Critério 2: Deve conter pelo menos uma letra
   
    if not any(char.isalpha() for char in senha):
        
        mensagens_erro.append("A senha deve conter pelo menos uma letra (a-z, A-Z).")

    # Critério 3: Deve conter pelo menos um número
    
    if not any(char.isdigit() for char in senha):
        
        mensagens_erro.append("A senha deve conter pelo menos um número (0-9).")
    
    # Se não houver mensagens de erro, a senha é forte
    if not mensagens_erro:
        return True, []
    else:
        return False, mensagens_erro

# Exemplo de uso:
if __name__ == "__main__":
    print("Verificador de Força de Senha (Números e Letras)")
    print("Critérios para senha forte:")
    print("1. Mínimo de 8 caracteres.")
    print("2. Pelo menos uma letra.")
    print("3. Pelo menos um número.")
  

    senha_usuario = input("Digite a senha que deseja verificar: ")

    eh_forte, erros = verificar_forca_senha_numeros_letras(senha_usuario)

    if eh_forte:
        print("\n[+] Senha forte!")
    else:
        print("\n[-] Senha fraca. Motivos:")
        for erro in erros:
            print(f"  - {erro}")