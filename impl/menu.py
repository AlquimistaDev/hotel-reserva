import tkinter as tk  # Importamos la biblioteca Tkinter para crear interfaces gráficas.

# Definimos las acciones asociadas a las opciones de los menús.
def accion1():
    texto.configure(text='Has elegido la opción 1 del menú principal')  # Cambia el texto de la etiqueta.

def accion2():
    texto.configure(text='Has elegido la opción 2 del menú principal')  # Cambia el texto de la etiqueta.

def acciona():
    texto.configure(text='Has elegido la opción a del submenú')  # Cambia el texto de la etiqueta.

def accionb():
    texto.configure(text='Has elegido la opción b del submenú')  # Cambia el texto de la etiqueta.

# Creamos la ventana principal.
ventana = tk.Tk()
ventana.title('Ventana principal')  # Establece el título de la ventana.
ventana.geometry('800x600')  # Establece el tamaño de la ventana.

# Creamos una barra de menús y la añadimos a la ventana principal.
# Cada ventana solo puede tener una barra de menús.
barra_menus = tk.Menu(ventana)
ventana.config(menu=barra_menus)  # Configuramos la ventana para que use la barra de menús.

# Creamos un menú cuyo contenedor será la barra de menús.
menu = tk.Menu(barra_menus, tearoff=False)

# Añadimos opciones al menú indicando su nombre y acción asociada.
menu.add_command(label='Opción 1', command=accion1)  # Añade una opción al menú que ejecuta `accion1`.
menu.add_command(label='Opción 2', command=accion2)  # Añade una opción al menú que ejecuta `accion2`.

# Creamos un submenú.
submenu = tk.Menu(menu, tearoff=False)
submenu.add_command(label='Opción A', command=acciona)  # Añade una opción al submenú que ejecuta `acciona`.
submenu.add_command(label='Opción B', command=accionb)  # Añade una opción al submenú que ejecuta `accionb`.

# Añadimos el submenú al menú principal.
menu.add_cascade(label='Submenú', menu=submenu)  # Añade el submenú al menú principal bajo el nombre 'Submenú'.

# Añadimos una línea separadora y la opción de salir.
menu.add_separator()  # Añade una línea separadora al menú.
menu.add_command(label='Salir', command=ventana.destroy)  # Añade una opción al menú que cierra la ventana.

# Finalmente, añadimos el menú a la barra de menús.
barra_menus.add_cascade(label="Menú", menu=menu)  # Añade el menú a la barra de menús bajo el nombre 'Menú'.

# Añadimos una etiqueta para ver el efecto de los botones del menú.
texto = tk.Label(ventana, text='¡Hola, desde Código Pitón!')  # Creamos una etiqueta con un mensaje inicial.
texto.place(x=200, y=200)  # Posicionamos la etiqueta en la ventana.

if __name__ == '__main__':
    ventana.mainloop()  # Ejecutamos la ventana principal para que se mantenga abierta y responda a eventos.