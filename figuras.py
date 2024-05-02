#Aquí va el código de los métodos para la creación de las figuras
import matplotlib.pyplot as plt

def cuadrado(ax, punto, longitud):
    # Obtener coordenadas x, y del punto inicial
    x, y = punto

    # Coordenadas de los puntos del cuadrado
    ejeX = [x, x + longitud, x + longitud, x, x]
    ejeY = [y, y, y + longitud, y + longitud, y]

    # Dibujar el cuadrado
    ax.plot(ejeX, ejeY, 'b-', linewidth=2)