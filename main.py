productos = []
cantidades = []


def registrar_producto():
    nombre = input("Nombre del producto: ").strip()
    cantidad = int(input("Cantidad disponible: "))
    productos.append(nombre)
    cantidades.append(cantidad)


def mostrar_inventario():
    if len(productos) == 0:
        print("El inventario esta vacio.")
    else:
        for i in range(len(productos)):
            print(i + 1, productos[i], "-", cantidades[i])


def Buscar_producto():
    nombre_producto = input("Digite nombre del producto: ").strip()

    if nombre_producto in productos:
        i = productos.index(nombre_producto)
        print("Producto disponible")
        print("Cantidad disponible:", cantidades[i])
    else:
        print("Producto no disponible")


def modificar_cantidad():
    nombre_producto = input(
        "Digite el nombre del producto que desea modificar: "
    ).strip()

    if nombre_producto in productos:
        i = productos.index(nombre_producto)
        nueva_cantidad = int(input("Nueva cantidad: "))
        cantidades[i] = nueva_cantidad
        print("Cantidad despues de modificar:", cantidades[i])
    else:
        print("Producto no encontrado.")



def eliminar_producto():
    nombre_producto = input("Digite el producto que desea eliminar: ").strip()

    if nombre_producto in productos:
        i = productos.index(nombre_producto)
        eliminada = productos.pop(i)
        cantidades.pop(i)
        print("Se elimino:", eliminada)
        print("Productos finales:", productos)
    else:
        print("Producto no encontrado.")



def mostrar_productos():
    print("Productos registrados:", len(productos))


def producto_mayor_cantidad():
    if len(cantidades) > 0:
        mayor = max(cantidades)
        i = cantidades.index(mayor)
        print("Producto con mayor cantidad:", productos[i])
        print("Cantidad disponible:", mayor)
    else:
        print("No hay productos registrados.")


def salir_programa():
    print("Saliendo del programa...")


opcion = 0

while opcion != 8:
    print("\n--- GESTOR DE INVENTARIO ---")
    print("1. Registrar producto")
    print("2. Mostrar inventario")
    print("3. Buscar producto")
    print("4. Modificar cantidad")
    print("5. Eliminar producto")
    print("6. Mostrar cantidad de productos")
    print("7. Mostrar producto con mayor cantidad")
    print("8. Salir")

    opcion = int(input("Seleccione una opcion: "))

    if opcion == 1:
        registrar_producto()
    elif opcion == 2:
        mostrar_inventario()
    elif opcion == 3:
        Buscar_producto()
    elif opcion == 4:
        modificar_cantidad()
    elif opcion == 5:
        eliminar_producto()
    elif opcion == 6:
        mostrar_productos()
    elif opcion == 7:
        producto_mayor_cantidad()
    elif opcion == 8:
        salir_programa()
    else:
        print("Opcion no valida.")
