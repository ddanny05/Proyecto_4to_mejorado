import requests
from tkinter import messagebox



API_CLIENTES = "http://127.0.0.1:8000/api/clientes/"
def listar_clientes(tree_clientes):
    response = realizar_peticion("GET", API_CLIENTES)
    if response:
        clientes = response.json()
        tree_clientes.delete(*tree_clientes.get_children())  
        for cliente in clientes:
            tree_clientes.insert('', 'end', values=(cliente['cedula'], cliente['nombre'], cliente['apellido'], cliente['telefono'], cliente['direccion']))


def realizar_peticion(metodo, url, datos=None):
    try:
        if metodo == "GET":
            response = requests.get(url)
        elif metodo == "POST":
            response = requests.post(url, json=datos)
        elif metodo == "PUT":
            response = requests.put(url, json=datos)
        elif metodo == "DELETE":
            response = requests.delete(url)
        
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Error en la petición: {e}")
        return None


def agregar_cliente(campos, tree_clientes):
    if not all(campo.get().strip() for campo in campos.values()):
        messagebox.showerror("Error", "Todos los campos son obligatorios.")
        return
    
    datos = { key: campo.get() for key, campo in campos.items() }
    response = realizar_peticion("POST", API_CLIENTES, datos)
    
    if response and response.status_code == 201:
        messagebox.showinfo("Éxito", "Cliente agregado correctamente")
        listar_clientes(tree_clientes)

def actualizar_cliente(campos, tree_clientes):
    if not all(campo.get().strip() for campo in campos.values()):
        messagebox.showerror("Error", "Todos los campos son obligatorios.")
        return
    
    cedula = campos["cedula"].get()
    datos = { key: campo.get() for key, campo in campos.items() if key != "cedula" }
    response = realizar_peticion("PUT", f"{API_CLIENTES}{cedula}/", datos)
    print(f"{API_CLIENTES}{cedula}/")
    
    if response and response.status_code == 200:
        messagebox.showinfo("Éxito", "Cliente actualizado correctamente")
        listar_clientes(tree_clientes)

def eliminar_cliente(cedula, tree_clientes):
    print (cedula)
    response = realizar_peticion("DELETE", f"{API_CLIENTES}{cedula}/")
    print (f"{API_CLIENTES}{cedula}/")
    
    if response and response.status_code == 204:
        messagebox.showinfo("Éxito", "Cliente eliminado correctamente")
        listar_clientes(tree_clientes)

        #ubicar un metodo para poder obtener la cedula del registro selecionado;
