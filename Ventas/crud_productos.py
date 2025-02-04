import requests
from tkinter import messagebox

API_PRODUCTOS = "http://127.0.0.1:8000/api/productos/"

def listar_productos(tree_productos):
    response = requests.get(API_PRODUCTOS)
    if response.ok:
        productos = response.json()
        tree_productos.delete(*tree_productos.get_children())  
        for producto in productos:
            tree_productos.insert('', 'end', values=(producto['codigo'], producto['nombre'], producto['descripcion'], producto['precio'], producto['stock']))

def agregar_producto(campos, tree_productos):
    datos = { key: campo.get() for key, campo in campos.items() }
    response = requests.post(API_PRODUCTOS, json=datos)
    
    if response.status_code == 201:
        messagebox.showinfo("Éxito", "Producto agregado correctamente")
        listar_productos(tree_productos)

def actualizar_producto(campos, tree_productos):
    codigo = campos["codigo"].get()
    datos = { key: campo.get() for key, campo in campos.items() if key != "codigo" }
    response = requests.put(f"{API_PRODUCTOS}{codigo}/", json=datos)
    
    if response.status_code == 200:
        messagebox.showinfo("Éxito", "Producto actualizado correctamente")
        listar_productos(tree_productos)

def eliminar_producto(codigo, tree_productos):
    response = requests.delete(f"{API_PRODUCTOS}{codigo}/")
    
    if response.status_code == 204:
        messagebox.showinfo("Éxito", "Producto eliminado correctamente")
        listar_productos(tree_productos)
