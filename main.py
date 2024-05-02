#Aquí se encuentra el menú principal de la aplicación

import figuras
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg #Permite integrar matplotlib con tkinter
import tkinter as tk
import tkinter.font as tkFont #Para cambiar la fuente de los elementos de la interfaz

#Evita que el bucle se mantenga en ejecución
def cerrar():
    root.quit()
    root.destroy()

# Crea una ventana
root = tk.Tk()
root.title("Graficadora")
root.wm_minsize(width=1000, height=1000)

labelFont = tkFont.Font(family="Helvetica", size=20, weight="bold")
inputFont = tkFont.Font(family="Helvetica", size=20)

# Crea una figura vacía inicial, ax es el contenedor de los elementos gráficos
fig, ax = plt.subplots()

# Configura los límites para los ejes
ax.set_xlim(-20, 20)  # Tamaño máximo para el eje x
ax.set_ylim(-20, 20)  # Tamño máximo para el eje y

# Añadir etiquetas a los ejes
ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")
ax.axhline(y=0, color='black', linestyle='-', linewidth=1, alpha=0.8)  # Marca el eje horizontal
ax.axvline(x=0, color='black', linestyle='-', linewidth=1, alpha=0.8)  # Marca el eje vertical

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
menu = root.nametowidget(desplegable.menuname)
menu.config(font=inputFont)  # Aplicar la fuente al menú desplegable
desplegable.config(font=labelFont)  # Aplicar la fuente al select
desplegable.pack(anchor='w', padx=10, pady=10)

#Inputs para el punto inicial
framePunto = tk.Frame(root)
framePunto.pack(pady=10)  # Espacio vertical para separar los Frames
puntoLabel_Cuadrado = tk.Label(framePunto, text="Punto de partida:", font=labelFont)
puntoLabel_Cuadrado.pack(side='left', padx=10, pady=10)
puntoInput_Cuadrado = tk.Entry(framePunto, width=30, font=inputFont)
puntoInput_Cuadrado.pack(side='left', padx=10, pady=10)

#Inputs para el tamaño
frameAncho = tk.Frame(root)
frameAncho.pack(pady=10)  # Espacio vertical para separar los Frames
longLabel_Cuadrado = tk.Label(frameAncho, text="Longitud:", font=labelFont)
longLabel_Cuadrado.pack(side='left', padx=60, pady=10)
longInput_Cuadrado = tk.Entry(frameAncho, width=30, font=inputFont)
longInput_Cuadrado.pack(side='left', padx=10, pady=10)

# Ejecutar el bucle de eventos de Tkinter
root.protocol("WM_DELETE_WINDOW", cerrar)
tk.mainloop()