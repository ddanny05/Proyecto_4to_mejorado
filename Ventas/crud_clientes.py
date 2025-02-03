import requests
from tkinter import messagebox

API_CLIENTES = "http://127.0.0.1:8000/api/clientes/"

def listar_clientes(tree_clientes):
    response = requests.get(API_CLIENTES)
    if response.status_code == 200:
        clientes = response.json()
        tree_clientes.delete(*tree_clientes.get_children())
        for cliente in clientes:
            tree_clientes.insert('', 'end', values=(cliente['cedula'], cliente['nombre'], cliente['apellido'], cliente['telefono'], cliente['direccion']))
    else:
        messagebox.showerror("Error", "No se pudo obtener la lista de clientes")

def agregar_cliente(cedula, nombre, apellido, telefono, direccion):
    datos = {'cedula': cedula.get(), 'nombre': nombre.get(), 'apellido': apellido.get(), 'telefono': telefono.get(), 'direccion': direccion.get()}
    response = requests.post(API_CLIENTES, json=datos)
    if response.status_code == 201:
        messagebox.showinfo("Éxito", "Cliente agregado correctamente")
    else:
        messagebox.showerror("Error", "No se pudo agregar el cliente")

# Función para eliminar un cliente
def eliminar_cliente(cedula, tree_clientes):
    url = f"{API_CLIENTES}{cedula}/"
    response = requests.delete(url)
    if response.status_code == 204:
        messagebox.showinfo("Éxito", f"Cliente {cedula} eliminado correctamente.")
        listar_clientes(tree_clientes)  # Actualiza la lista de clientes
    else:
        messagebox.showerror("Error", f"No se pudo eliminar el cliente {cedula}.")
        
# Función para listar clientes (esto se llama después de eliminar)
def listar_clientes(tree_clientes):
    response = requests.get(API_CLIENTES)
    if response.status_code == 200:
        clientes = response.json()
        tree_clientes.delete(*tree_clientes.get_children())  # Limpiar el árbol
        for cliente in clientes:
            tree_clientes.insert('', 'end', values=(cliente['cedula'], cliente['nombre'], cliente['apellido'], cliente['telefono'], cliente['direccion']))
    else:
        messagebox.showerror("Error", "No se pudo obtener la lista de clientes")
