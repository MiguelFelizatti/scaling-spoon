def verificar_letra_a(s):
    # Contar a ocorrência de "a" e "A"
    contagem_minuscula = s.lower().count('a')
    contagem_maiuscula = s.upper().count('A')

    #Soma das contagens
    total_ocorrencias = contagem_maiuscula + contagem_minuscula

    if total_ocorrencias > 0:
        return True, total_ocorrencias
    else:
        return False, 0 
    
#Solicita ao usuário para informar uma string
entrada = input("Digite uma string para verificar a ocorrência da letra 'a':")

# Verifica a ocorrência da letra 'a'
existe, quantidade = verificar_letra_a(entrada)

if existe:
    print(f"A letra 'a' ocorre {quantidade} vez(es) na string.")
else:
    print("A letra 'a' não ocorre na string.")