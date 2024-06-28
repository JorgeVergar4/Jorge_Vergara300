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
