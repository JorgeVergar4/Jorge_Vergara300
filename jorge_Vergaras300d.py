
import csv
import os
import time
import funciones_Jorge_Vergara300d as funcionestest

precios_productos = {
    "Margaritas $1100":1100,
    "Rosas rojas $1700": 1700,
    "Lirio $1100": 1100,
    "Tierra $1000": 1000,
    "Abono $1200": 1200
}

def registrar_pedido():
    cliente = {}
    pedidos = []
    
    print("Ingrese la información del cliente:")
    cliente["nombre"] = input("Nombre: ")
    cliente["direccion"] = input("Dirección: ")
    cliente["telefono"] = input("Telefono: ")

    if  cliente["nombre"]=='' and cliente["direccion"] =='' and cliente["telefono"] =='':
         cliente["nombre"] = input("Ingrese su nombre correctamente: ")
         cliente["direccion"] = input("dirección: ")
         cliente["telefono"] = input("Telefono: ")
    else:
        print("Ingreso todos los datos correctamente sera redirigido a los detalles de pedido")

    while True:
        print("\nIngrese los detalles del pedido:")
        print("Elija el tipo de producto:")
        for i, producto in enumerate(precios_productos, start=1):
            print(f"{i}. {producto}")
        seleccion = int(input("Seleccione el número de producto: "))
        producto_seleccionado = list(precios_productos.keys())[seleccion - 1]
        cantidad = int(input(f"Ingrese la cantidad de '{producto_seleccionado}': "))

        pedido = {
            "producto": producto_seleccionado,
            "cantidad": cantidad
        }

        pedidos.append(pedido)

        continuar = input("¿Desea añadir más productos al pedido? (si/no): ")
        if continuar.lower() != 'si':
            break

    guardar_pedido(cliente, pedidos)

def guardar_pedido(cliente, pedidos):
    try:
        with open('pedidos.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            if file.tell() == 0:
                writer.writerow(["Nombre", "Direccion", "Telefono", "Producto", "Cantidad", "Precio Unitario", "Total"])
            
            total_pedido = 0
            
            for pedido in pedidos:
                precio_unitario = precios_productos[pedido["producto"]]
                total = precio_unitario * pedido["cantidad"]
                total_pedido += total
                writer.writerow([cliente["nombre"], cliente["direccion"], cliente["telefono"],
                                 pedido["producto"], pedido["cantidad"], precio_unitario, total])
            
            print(f"\nPedido registrado correctamente. Total a pagar: ${total_pedido}")
    except IOError:
        print("Error al escribir en el archivo CSV.")

 
def listar_pedidos():
    try:
        with open('pedidos.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except IOError:
        print("Error al leer el archivo CSV.")

def main():
    while True:

        print("Sistema de Gestión de Pedidos GreenGarden")
        print("1. Registrar Pedido")
        print("2. Listar Pedidos")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        os.system('cls')
        time.sleep(1)

        if opcion == '1':
            registrar_pedido()
        elif opcion == '2':
            listar_pedidos()
        elif opcion == '3':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida (1-3).")  
            time.sleep(2)

if __name__ == "__main__":
    main()
