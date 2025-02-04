import tkinter as tk
from tkinter import ttk, messagebox
import requests

API_CLIENTES = "http://127.0.0.1:8000/api/clientes/"

# Función para listar los clientes
def listar_clientes(tree_clientes):
    response = requests.get(API_CLIENTES)
    if response.status_code == 200:
        clientes = response.json()
        tree_clientes.delete(*tree_clientes.get_children())  # Limpiar el Treeview
        for cliente in clientes:
            tree_clientes.insert('', 'end', values=(cliente['cedula'], cliente['nombre'], cliente['apellido'], cliente['telefono'], cliente['direccion']))
    else:
        messagebox.showerror("Error", "No se pudo obtener la lista de clientes")

# Función para agregar un cliente
def agregar_cliente(cedula, nombre, apellido, telefono, direccion, tree_clientes):
    # Validar los datos (asegúrate de que los campos no estén vacíos)
    if not cedula.get() or not nombre.get() or not apellido.get() or not telefono.get() or not direccion.get():
        messagebox.showerror("Error", "Todos los campos son obligatorios.")
        return
    
    # Preparar los datos a enviar al API
    datos = {
        'cedula': cedula.get(),
        'nombre': nombre.get(),
        'apellido': apellido.get(),
        'telefono': telefono.get(),
        'direccion': direccion.get()
    }
    
    # Hacer el POST al API
    response = requests.post(API_CLIENTES, json=datos)
    
    if response.status_code == 201:
        messagebox.showinfo("Éxito", "Cliente agregado correctamente")
        listar_clientes(tree_clientes)  # Actualiza la lista de clientes
    else:
        messagebox.showerror("Error", "No se pudo agregar el cliente")

# Función para actualizar un cliente
def actualizar_cliente(cedula, nombre, apellido, telefono, direccion, tree_clientes):
    datos = {
        'nombre': nombre.get(),
        'apellido': apellido.get(),
        'telefono': telefono.get(),
        'direccion': direccion.get()
    }

    response = requests.put(f"{API_CLIENTES}{cedula}/", json=datos)
    
    if response.status_code == 200:
        messagebox.showinfo("Éxito", "Cliente actualizado correctamente")
        listar_clientes(tree_clientes)
    else:
        messagebox.showerror("Error", "No se pudo actualizar el cliente")

# Función para eliminar un cliente
def eliminar_cliente(cedula, tree_clientes):
    response = requests.delete(f"{API_CLIENTES}{cedula}/")
    
    if response.status_code == 204:
        messagebox.showinfo("Éxito", "Cliente eliminado correctamente")
        listar_clientes(tree_clientes)
    else:
        messagebox.showerror("Error", "No se pudo eliminar el cliente")
