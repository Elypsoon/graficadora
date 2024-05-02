import re

t1 = "(99,2)"
t2 = "100"
t3 = "0"

lista_de_tokens = [t1,t2,t3]

def validar_token(token,opc=1):
    
    if opc == 1:
        #patron = r"^\(([0-99]),\s*([0-9])\)$"
        patron = patron = r"^\((100|[1-9][0-9]?|0),\s*(100|[1-9][0-9]?|0)\)$"

    if opc == 2:
        #patron = r"^[1-9]$" # Del 1 al 9
        patron = r"^(100|[1-9][0-9]?|0)$" # Del 0 al 100

    if re.match(patron, token):
        return True

def analizador(lista_de_tokens):

    # Obtenemos el Tamaño de la lista de Tokens
    size = len(lista_de_tokens)

    # Comprobamos Tamaño de la Lista
    if size == 0:
        print("No Tokens")
        return False
    else:
        print("Tokens")
        
    # Recorremos la Lista de Tokens
    for token in lista_de_tokens:
        if lista_de_tokens.index(token) == 0:
            print("\nToken Base")
            print(token)
            r = validar_token(token, 1)
            print(r)
        else:
            print("\nToken Secundario")
            print(token)
            r = validar_token(token, 2)
            print(r)
    
    #base = lista_de_tokens[0]
    #base = str(base)
    #print(base)

    # if validar_token(base, 1):
    #     print("Token válido")
    # else:
    #     print("Token inválido")
                
analizador(lista_de_tokens)

