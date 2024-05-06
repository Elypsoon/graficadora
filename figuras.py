#Aquí va el código de los métodos para la creación de las figuras
import matplotlib.pyplot as plt

def cuadrado(ax, punto, longitud):
    # Obtener coordenadas x, y del punto donde partirá el cuadrado
    x, y = punto

    # Coordenadas de los puntos del cuadrado
    ejeX = [x, x + longitud, x + longitud, x, x]
    ejeY = [y, y, y + longitud, y + longitud, y]

    # Añaadir el cuadrado al eje
    ax.plot(ejeX, ejeY, 'b-', linewidth=2)
    
def circulo(ax, punto, radio):
    # Obtener coordenadas x, y del punto central
    x, y = punto

    # Crear un círculo con centro en (x, y)
    circulo = plt.Circle((x, y), radio, color='r', fill=False, linewidth=2)

    # Añadir el círculo al eje
    ax.add_artist(circulo)
    ax.relim()  # Recalcular límites basándose en las figuras actuales
    ax.autoscale_view()  # Ajustar la escala para asegurar que todo sea visible

def triangulo(ax, punto, longitud):
    # Obtener coordenadas x, y del punto donde partirá el triángulo
    x, y = punto

    # Coordenadas de los puntos del triángulo
    ejeX = [x, x + longitud, x + longitud/2, x]
    ejeY = [y, y, y + longitud, y]

    # Añaadir el triángulo al eje
    ax.plot(ejeX, ejeY, 'g-', linewidth=2)
    
def rectangulo(ax, punto, ancho, alto):
    # Obtener coordenadas x, y del punto donde partirá el rectángulo
    x, y = punto

    # Coordenadas de los puntos del rectángulo
    ejeX = [x, x + ancho, x + ancho, x, x]
    ejeY = [y, y, y + alto, y + alto, y]

    # añaadir el rectángulo al eje
    ax.plot(ejeX, ejeY, 'y-', linewidth=2)