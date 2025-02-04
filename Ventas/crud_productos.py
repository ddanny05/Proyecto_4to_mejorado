import tkinter as tk
from tkinter import ttk, messagebox
import requests

API_PRODUCTOS = "http://127.0.0.1:8000/api/productos/"

# Función para listar los productos
def listar_productos(tree_productos):
    response = requests.get(API_PRODUCTOS)
    if response.status_code == 200:
        productos = response.json()
        tree_productos.delete(*tree_productos.get_children())  # Limpiar el Treeview
        for producto in productos:
            tree_productos.insert('', 'end', values=(producto['codigo'], producto['nombre'], producto['descripcion'], producto['precio'], producto['stock']))
    else:
        messagebox.showerror("Error", "No se pudo obtener la lista de productos")

# Función para agregar un producto
def agregar_producto(nombre, descripcion, precio, stock, tree_productos):
    # Validar los datos (asegúrate de que los campos no estén vacíos)
    if not nombre.get() or not descripcion.get() or not precio.get() or not stock.get():
        messagebox.showerror("Error", "Todos los campos son obligatorios.")
        return
    
    # Preparar los datos a enviar al API
    datos = {
        'codigo': 'GENERADO_CODIGO',  # Genera un código o déjalo al API
        'nombre': nombre.get(),
        'descripcion': descripcion.get(),
        'precio': precio.get(),
        'stock': stock.get()
    }
    
    # Hacer el POST al API
    response = requests.post(API_PRODUCTOS, json=datos)
    
    if response.status_code == 201:
        messagebox.showinfo("Éxito", "Producto agregado correctamente")
        listar_productos(tree_productos)  # Actualiza la lista de productos
    else:
        messagebox.showerror("Error", "No se pudo agregar el producto")

# Función para actualizar un producto
def actualizar_producto(codigo, nombre, descripcion, precio, stock, tree_productos):
    datos = {
        'nombre': nombre.get(),
        'descripcion': descripcion.get(),
        'precio': precio.get(),
        'stock': stock.get()
    }

    response = requests.put(f"{API_PRODUCTOS}{codigo}/", json=datos)
    
    if response.status_code == 200:
        messagebox.showinfo("Éxito", "Producto actualizado correctamente")
        listar_productos(tree_productos)
    else:
        messagebox.showerror("Error", "No se pudo actualizar el producto")

# Función para eliminar un producto
def eliminar_producto(codigo, tree_productos):
    response = requests.delete(f"{API_PRODUCTOS}{codigo}/")
    
    if response.status_code == 204:
        messagebox.showinfo("Éxito", "Producto eliminado correctamente")
        listar_productos(tree_productos)
    else:
        messagebox.showerror("Error", "No se pudo eliminar el producto")
