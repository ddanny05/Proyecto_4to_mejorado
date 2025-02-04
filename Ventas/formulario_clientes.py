import tkinter as tk
from tkinter import ttk, messagebox
from crud_clientes import listar_clientes, agregar_cliente, actualizar_cliente, eliminar_cliente

def abrir_crud_clientes():
    ventana = tk.Toplevel()
    ventana.title("Gestión de Clientes")
    ventana.geometry("600x400")

    frame_form = ttk.LabelFrame(ventana, text="Formulario Cliente")
    frame_form.pack(pady=10, padx=10, fill="x")
    
    campos = {}
    etiquetas = ["Cédula", "Nombre", "Apellido", "Teléfono", "Dirección"]
    
    for i, label in enumerate(etiquetas):
        ttk.Label(frame_form, text=label + ":").grid(row=i, column=0, padx=5, pady=5, sticky="w")
        campo = tk.StringVar()
        ttk.Entry(frame_form, textvariable=campo).grid(row=i, column=1, padx=5, pady=5)
        campos[label.lower()] = campo

    btn_frame = ttk.Frame(ventana)
    btn_frame.pack(pady=10)

    tree_clientes = ttk.Treeview(ventana, columns=etiquetas, show="headings")
    
    for col in etiquetas:
        tree_clientes.heading(col, text=col)
        tree_clientes.column(col, width=100)

    tree_clientes.pack(fill="both", expand=True)

    listar_clientes(tree_clientes)

    ttk.Button(btn_frame, text="Agregar", command=lambda: agregar_cliente(campos, tree_clientes)).pack(side=tk.LEFT, padx=5)
    ttk.Button(btn_frame, text="Actualizar", command=lambda: actualizar_cliente(campos, tree_clientes)).pack(side=tk.LEFT, padx=5)
    ttk.Button(btn_frame, text="Eliminar", command=lambda: eliminar_cliente(campos['cédula'].get(), tree_clientes)).pack(side=tk.LEFT, padx=5)

    ventana.mainloop()  # Asegura que la ventana se mantenga abierta
