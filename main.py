#Aquí se encuentra el menú principal de la aplicación

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg #Permite integrar matplotlib con tkinter
import tkinter as tk

#Evita que el bucle se mantenga en ejecución
def cerrar():
    root.quit()
    root.destroy()

# Crea una ventana
root = tk.Tk()
root.title("Graficadora")
root.wm_minsize(width=1200, height=800)

# Crea una figura vacía inicial
fig, ax = plt.subplots()

# Configura los límites para los ejes
ax.set_xlim(0, 20)  # Límites para el eje x
ax.set_ylim(0, 20)  # Límites para el eje y

# Añadir etiquetas a los ejes
ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")

# Añadir cuadrícula
ax.grid(True)

# Crear lienzo para Matplotlib
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()

# Inserta el lienzo en la ventana
canvas.get_tk_widget().pack(expand=True, fill=tk.BOTH)

# Ejecutar el bucle de eventos de Tkinter
root.protocol("WM_DELETE_WINDOW", cerrar)

tk.mainloop()
