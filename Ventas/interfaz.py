import tkinter as tk
from tkinter import ttk, messagebox
from crud_clientes import listar_clientes, agregar_cliente, eliminar_cliente, actualizar_cliente
from crud_productos import listar_productos, agregar_producto, eliminar_producto, actualizar_producto

# Función para abrir el formulario de agregar cliente
def formulario_agregar_cliente():
    ventana_agregar = tk.Toplevel(ventana)
    ventana_agregar.title("Agregar Cliente")
    ventana_agregar.geometry("300x300")

    tk.Label(ventana_agregar, text="Cédula").pack()
    cedula = tk.StringVar()
    tk.Entry(ventana_agregar, textvariable=cedula).pack()

    tk.Label(ventana_agregar, text="Nombre").pack()
    nombre = tk.StringVar()
    tk.Entry(ventana_agregar, textvariable=nombre).pack()

    tk.Label(ventana_agregar, text="Apellido").pack()
    apellido = tk.StringVar()
    tk.Entry(ventana_agregar, textvariable=apellido).pack()

    tk.Label(ventana_agregar, text="Teléfono").pack()
    telefono = tk.StringVar()
    tk.Entry(ventana_agregar, textvariable=telefono).pack()

    tk.Label(ventana_agregar, text="Dirección").pack()
    direccion = tk.StringVar()
    tk.Entry(ventana_agregar, textvariable=direccion).pack()

    tk.Button(ventana_agregar, text="Agregar", command=lambda: agregar_cliente(cedula, nombre, apellido, telefono, direccion)).pack()

# Función para abrir el formulario de listar clientes
def formulario_clientes():
    ventana_clientes = tk.Toplevel(ventana)
    ventana_clientes.title("Lista de Clientes")
    ventana_clientes.geometry("600x400")

    columnas = ("Cédula", "Nombre", "Apellido", "Teléfono", "Dirección")
    tree_clientes = ttk.Treeview(ventana_clientes, columns=columnas, show="headings")
    for col in columnas:
        tree_clientes.heading(col, text=col)
    tree_clientes.pack(fill=tk.BOTH, expand=True)

    listar_clientes(tree_clientes)

# Función para abrir el formulario de agregar producto
def formulario_agregar_producto():
    ventana_agregar = tk.Toplevel(ventana)
    ventana_agregar.title("Agregar Producto")
    ventana_agregar.geometry("300x300")

    tk.Label(ventana_agregar, text="Código").pack()
    codigo = tk.StringVar()
    tk.Entry(ventana_agregar, textvariable=codigo).pack()

    tk.Label(ventana_agregar, text="Nombre Producto").pack()
    nombre_producto = tk.StringVar()
    tk.Entry(ventana_agregar, textvariable=nombre_producto).pack()

    tk.Label(ventana_agregar, text="Descripción").pack()
    descripcion = tk.StringVar()
    tk.Entry(ventana_agregar, textvariable=descripcion).pack()

    tk.Label(ventana_agregar, text="Precio").pack()
    precio = tk.StringVar()
    tk.Entry(ventana_agregar, textvariable=precio).pack()

    tk.Label(ventana_agregar, text="Stock").pack()
    stock = tk.StringVar()
    tk.Entry(ventana_agregar, textvariable=stock).pack()

    tk.Button(ventana_agregar, text="Agregar", command=lambda: agregar_producto(codigo, nombre_producto, descripcion, precio, stock)).pack()

# Función para abrir el formulario de listar productos
def formulario_productos():
    ventana_productos = tk.Toplevel(ventana)
    ventana_productos.title("Lista de Productos")
    ventana_productos.geometry("600x400")

    columnas = ("Código", "Nombre", "Descripción", "Precio", "Stock")
    tree_productos = ttk.Treeview(ventana_productos, columns=columnas, show="headings")
    for col in columnas:
        tree_productos.heading(col, text=col)
    tree_productos.pack(fill=tk.BOTH, expand=True)

    listar_productos(tree_productos)

# Función para eliminar cliente
# Eliminar Cliente (asegúrate de que esto esté dentro de la lógica de tu interfaz)

def eliminar_cliente_interface():
    selected_item = tree_clientes.selection()
    if selected_item:
        cedula = tree_clientes.item(selected_item)["values"][0]  # Cédula del cliente seleccionado
        eliminar_cliente(cedula, tree_clientes)
    else:
        messagebox.showwarning("Selección", "Debe seleccionar un cliente para eliminar.")

# Función para eliminar producto
def eliminar_producto_interface():
    selected_item = tree_productos.selection()
    if selected_item:
        codigo = tree_productos.item(selected_item)["values"][0]  # Código del producto seleccionado
        eliminar_producto(codigo, tree_productos)
    else:
        messagebox.showwarning("Selección", "Debe seleccionar un producto para eliminar.")

# Ventana principal
ventana = tk.Tk()
ventana.title("Gestión de Clientes y Productos")
ventana.geometry("800x600")

# Crear menú principal
menu = tk.Menu(ventana)
ventana.config(menu=menu)

# Menú Clientes
menu_clientes = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Clientes", menu=menu_clientes)
menu_clientes.add_command(label="Agregar Cliente", command=formulario_agregar_cliente)
menu_clientes.add_command(label="Listar Clientes", command=formulario_clientes)

# Menú Productos
menu_productos = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Productos", menu=menu_productos)
menu_productos.add_command(label="Listar Productos", command=formulario_productos)
menu_productos.add_command(label="Agregar Producto", command=formulario_agregar_producto)

# Iniciar la aplicación
ventana.mainloop()
