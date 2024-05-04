#Aquí va el código de los métodos para la creación de las figuras
import matplotlib.pyplot as plt

estado = {'cuadrado': None, 'circulo': None, 'triangulo': None, 'rectangulo': None}

def cuadrado(ax, punto, longitud):
    # Obtener coordenadas x, y del punto donde partirá el cuadrado
    x, y = punto

    # Coordenadas de los puntos del cuadrado
    ejeX = [x, x + longitud, x + longitud, x, x]
    ejeY = [y, y, y + longitud, y + longitud, y]

    # Añaadir el cuadrado al eje
    estado['cuadrado'] = ax.plot(ejeX, ejeY, 'b-', linewidth=2)
    
def circulo(ax, punto, radio):
    # Obtener coordenadas x, y del punto central
    x, y = punto

    # Crear un círculo con centro en (x, y)
    circulo = plt.Circle((x, y), radio, color='r', fill=False, linewidth=2)

    # Añadir el círculo al eje
    estado['circulo'] = ax.add_artist(circulo)

def triangulo(ax, punto, longitud):
    # Obtener coordenadas x, y del punto donde partirá el triángulo
    x, y = punto

    # Coordenadas de los puntos del triángulo
    ejeX = [x, x + longitud, x + longitud/2, x]
    ejeY = [y, y, y + longitud, y]

    # Añaadir el triángulo al eje
    estado['triangulo'] = ax.plot(ejeX, ejeY, 'g-', linewidth=2)
    
def rectangulo(ax, punto, ancho, alto):
    # Obtener coordenadas x, y del punto donde partirá el rectángulo
    x, y = punto

    # Coordenadas de los puntos del rectángulo
    ejeX = [x, x + ancho, x + ancho, x, x]
    ejeY = [y, y, y + alto, y + alto, y]

    # añaadir el rectángulo al eje
    estado['rectangulo'] = ax.plot(ejeX, ejeY, 'y-', linewidth=2)