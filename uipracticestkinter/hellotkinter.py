import tkinter as tk

ventana = tk.Tk()
ventana.title("Hola Tkinter")
ventana.geometry("400x300")

etiqueta = tk.Label(ventana, text="¡Hola, mundo!")
etiqueta.pack(pady=20)

boton = tk.Button(ventana, text="Salir", command=ventana.quit)
boton.pack()

ventana.mainloop()