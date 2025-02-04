import tkinter as tk
from formulario_clientes import abrir_crud_clientes
from formulario_productos import abrir_crud_productos

def main():
    root = tk.Tk()
    root.title("Sistema de Gestión")
    root.geometry("800x600")
    
    # Menú principal
    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)
    
    menu_clientes = tk.Menu(menu_bar, tearoff=0)
    menu_clientes.add_command(label="Gestión de Clientes", command=abrir_crud_clientes)
    menu_bar.add_cascade(label="Clientes", menu=menu_clientes)
    
    menu_productos = tk.Menu(menu_bar, tearoff=0)
    menu_productos.add_command(label="Gestión de Productos", command=abrir_crud_productos)
    menu_bar.add_cascade(label="Productos", menu=menu_productos)
    
    root.mainloop()

if __name__ == "__main__":
    main()
