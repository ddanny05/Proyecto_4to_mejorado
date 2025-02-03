import requests
from tkinter import messagebox

API_PRODUCTOS = "http://127.0.0.1:8000/api/productos/"

def listar_productos(tree_productos):
    response = requests.get(API_PRODUCTOS)
    if response.status_code == 200:
        productos = response.json()
        tree_productos.delete(*tree_productos.get_children())
        for producto in productos:
            tree_productos.insert('', 'end', values=(producto['codigo'], producto['nombre'], producto['descripcion'], producto['precio'], producto['stock']))
    else:
        messagebox.showerror("Error", "No se pudo obtener la lista de productos")

def agregar_producto(codigo, nombre_producto, descripcion, precio, stock):
    datos = {'codigo': codigo.get(), 'nombre': nombre_producto.get(), 'descripcion': descripcion.get(), 'precio': precio.get(), 'stock': stock.get()}
    response = requests.post(API_PRODUCTOS, json=datos)
    if response.status_code == 201:
        messagebox.showinfo("Éxito", "Producto agregado correctamente")
    else:
        messagebox.showerror("Error", "No se pudo agregar el producto")

# Función para eliminar un producto
def eliminar_producto(codigo, tree_productos):
    url = f"{API_PRODUCTOS}{codigo}/"
    response = requests.delete(url)
    if response.status_code == 204:
        messagebox.showinfo("Éxito", f"Producto {codigo} eliminado correctamente.")
        listar_productos(tree_productos)  # Actualiza la lista de productos
    else:
        messagebox.showerror("Error", f"No se pudo eliminar el producto {codigo}.")
        
# Función para listar productos (esto se llama después de eliminar)
def listar_productos(tree_productos):
    response = requests.get(API_PRODUCTOS)
    if response.status_code == 200:
        productos = response.json()
        tree_productos.delete(*tree_productos.get_children())  # Limpiar el árbol
        for producto in productos:
            tree_productos.insert('', 'end', values=(producto['codigo'], producto['nombre'], producto['descripcion'], producto['precio'], producto['stock']))
    else:
        messagebox.showerror("Error", "No se pudo obtener la lista de productos")
