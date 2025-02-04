import tkinter as tk
from tkinter import ttk, messagebox
from crud_productos import listar_productos, agregar_producto, actualizar_producto, eliminar_producto

def abrir_crud_productos():
    ventana = tk.Toplevel()
    ventana.title("Gestión de Productos")
    ventana.geometry("600x400")

    frame_form = ttk.LabelFrame(ventana, text="Formulario Producto")
    frame_form.pack(pady=10, padx=10, fill="x")

    campos = {}
    etiquetas = ["Código", "Nombre", "Descripción", "Precio", "Stock"]
    
    for i, label in enumerate(etiquetas):
        ttk.Label(frame_form, text=label + ":").grid(row=i, column=0, padx=5, pady=5, sticky="w")
        campo = tk.StringVar()
        ttk.Entry(frame_form, textvariable=campo).grid(row=i, column=1, padx=5, pady=5)
        campos[label.lower()] = campo

    btn_frame = ttk.Frame(ventana)
    btn_frame.pack(pady=10)

    tree_productos = ttk.Treeview(ventana, columns=etiquetas, show="headings")

    for col in etiquetas:
        tree_productos.heading(col, text=col)
        tree_productos.column(col, width=100)

    tree_productos.pack(fill="both", expand=True)

    listar_productos(tree_productos)

    ttk.Button(btn_frame, text="Agregar", command=lambda: agregar_producto(campos, tree_productos)).pack(side=tk.LEFT, padx=5)
    ttk.Button(btn_frame, text="Actualizar", command=lambda: actualizar_producto(campos, tree_productos)).pack(side=tk.LEFT, padx=5)
    ttk.Button(btn_frame, text="Eliminar", command=lambda: eliminar_producto(campos['código'].get(), tree_productos)).pack(side=tk.LEFT, padx=5)

    ventana.mainloop()  # Asegura que la ventana se mantenga abierta
