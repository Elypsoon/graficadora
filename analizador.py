import re

lista_tokens = [] # Lista de Tokens

# Diccionario de Errores
diccionario_errores = {
    1: [],
    2: [],
    3: [],
    4: []
}

# Códigos de Errores
errores = {
    "0": "\n  ¡Errores Input 1!\n\n > Debe Iniciar con Paréntesis de Apertura",
    "1": "\n > Debe Finalizar con Paréntesis de Cierre",
    "2": "\n > Coma no Encontrada, Mal Posicionada o Estructura Inválida",
    "3": "\n > Más de una Coma Encontrada",
    "4": "\n > No se Encontró Número Valido",
    "5": "\n  ¡Error Input 2 o 3!\n\n > La Cadena Debe Contener un Número Válido"
}

# Función para Obtener Mensajes de Errores
def obtener_mensajes_errores_clave(diccionario_errores, clave):
    mensajes_errores = ""
    if clave in diccionario_errores:
        lista_errores = diccionario_errores[clave]
        for codigo_error in lista_errores:
            if codigo_error in errores:
                mensajes_errores += f"{errores[codigo_error]}\n"
            else:
                mensajes_errores += f"Error Desconocido: {codigo_error}\n"
    else:
        mensajes_errores = "Clave no Encontrada en el Diccionario de Errores"
    return mensajes_errores

# Función para Validar Tokens
def validar_token(token, opc, clave):

    if opc == 1:

        if not (re.match(r"^\(", token)):
            diccionario_errores[clave].append("0")  # No Inicia con Parentesis
            
        if not (re.match(r".*\)$", token)):
            diccionario_errores[clave].append("1") # No Finaliza con Parentesis

        if not (re.search(r"\(([^)]+),([^)]+)\)", token)):
            diccionario_errores[clave].append("2") # No Contiene una coma Valida

        if(re.search(r",.*,", token)):
            diccionario_errores[clave].append("3") # Contiene más de una Coma
        
        if len(diccionario_errores[clave]) == 0:
            patron = r"\(([^)]+),([^)]+)\)"
            numeros = re.sub(patron, r"\1,\2", token)

            for numero in numeros.split(","):
                try:
                    float(numero)
                except:
                    diccionario_errores[clave].append("4") # No es un Número
        
        if len(diccionario_errores[clave]) == 0:
            return True
        else:
            return False

    if opc == 2:
        try:
            float(token)
            return True
        except ValueError:
                diccionario_errores[clave].append("5") # No es un Número
                return False

# Función Principal
def analizador(lista_tokens, clave):
    
    # Recorremos la Lista de Tokens
    for token in lista_tokens:
        if lista_tokens.index(token) == 0: # Token Base
            validar_token(token, 1, clave)
        else: # Token Secundario
            validar_token(token, 2, clave)
                
    if len(diccionario_errores[clave]) == 0:
        return True