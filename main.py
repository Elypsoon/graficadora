#Aquí se encuentra el menú principal de la aplicación

import figuras
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg #Permite integrar matplotlib con tkinter
import tkinter as tk
import tkinter.font as tkFont


#Evita que el bucle se mantenga en ejecución
def cerrar():
    root.quit()
    root.destroy()

# Crea una ventana
root = tk.Tk()
root.title("Graficadora")
root.wm_minsize(width=1000, height=1000)

# Crea una figura vacía inicial, ax es el contenedor de los elementos gráficos
fig, ax = plt.subplots()

# Configura los límites para los ejes
ax.set_xlim(0, 20)  # Tamaño máximo para el eje x
ax.set_ylim(0, 20)  # Tamño máximo para el eje y

# Añadir etiquetas a los ejes
ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")

# Añadir cuadrícula
ax.grid(True)

# Crear lienzo para Matplotlib
canvas = FigureCanvasTkAgg(fig, master=root)

figuras.cuadrado(ax, (2, 2), 5)
figuras.circulo(ax, (10, 10), 3)
figuras.triangulo(ax, (3, 10), 5)
figuras.rectangulo(ax, (10, 3), 4, 6)

canvas.draw()

# Inserta el lienzo en la ventana
canvas.get_tk_widget().pack(expand=True, fill=tk.BOTH)

#Para el desplegable
select = tk.StringVar(value="Cuadrado")
opciones = ["Cuadrado", "Rectángulo", "Triángulo", "Círculo"]
desplegable = tk.OptionMenu(root, select, *opciones)
desplegable.config(font=tkFont.Font(family="Helvetica", size=20, weight="bold"))  # Aplicar la fuente al OptionMenu
desplegable.pack(anchor='w', padx=10, pady=10)

#Inputs para el punto inicial
puntoLabel_Cuadrado = tk.Label(root, text="Punto de partida:", font=tkFont.Font(family="Helvetica", size=20, weight="bold"))
puntoLabel_Cuadrado.pack(side='left', padx=10, pady=10)
puntoInput_Cuadrado = tk.Entry(root, width=30, font=tkFont.Font(family="Helvetica", size=20))
puntoInput_Cuadrado.pack(side='left', padx=10, pady=10)

# Ejecutar el bucle de eventos de Tkinter
root.protocol("WM_DELETE_WINDOW", cerrar)
tk.mainloop()