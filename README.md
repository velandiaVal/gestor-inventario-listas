# gestor-inventario-listas
Programa en Python - Gestionar el inventario de una tienda
Gestor de inventario con listas en Python

1. Objetivo del programa
El objetivo del proyecto es desarrollar un programa en Python que permita administrar el inventario de una tienda pequeña. El programa permite registrar productos y sus cantidades disponibles, consultar el inventario, buscar productos por su nombre, modificar cantidades, eliminar productos y obtener un resumen del inventario.
En este proyecto se busca practicar un poco del funcionamiento de listas, índices, ciclos, condicionales y funciones en Python.

2. Requisitos para ejecutar el programa
Para ejecutar el programa se necesita:

▹ Tener Python instalado en el computador.

▹ Contar con un editor de código, como Visual Studio Code, o una terminal que permita ejecutar Python.

▹ Descargar o clonar el repositorio de GitHub.

▹ Ejecutar el archivo main.py.

▹ El programa utiliza funciones y listas propias en Python, por lo que no necesitamos instalar librerías externas.


3. Instrucciones de uso
   
▹ Ejecutar el archivo main.py.

▹ Esperar a que aparezca el menú principal del gestor de inventario.

▹ Escribir el número de la opción que se desea utilizar.

▹ Seguir las instrucciones que aparecen en pantalla para ingresar los nombres de los productos y sus cantidades.

▹ Utilizar las opciones del menú para registrar, consultar, buscar, modificar o eliminar productos.

▹ Consultar la cantidad total de productos registrados o identificar el producto con la mayor cantidad disponible.

▹ Seleccionar la opción 8 para salir del programa.

 Los datos se mantienen durante la ejecución del programa. Al cerrarlo, el inventario no se conserva para la siguiente ejecución.

4. Funciones implementadas
   
▹ registrar_producto(): solicita el nombre del producto y su cantidad disponible, y guarda ambos datos en sus respectivas listas.

▹ mostrar_inventario(): muestra los productos registrados junto con sus cantidades. Si no hay productos, informa que el inventario está    vacío.

▹ Buscar_producto(): busca un producto por su nombre e informa si está registrado y qué cantidad tiene disponible.

▹ modificar_cantidad(): permite buscar un producto y actualizar la cantidad disponible.

▹ eliminar_producto(): verifica si el producto existe y, si está registrado, lo elimina del inventario junto con su cantidad  
.
▹ mostrar_productos(): muestra la cantidad de productos registrados en el inventario.

▹ producto_mayor_cantidad(): identifica el producto que tiene la mayor cantidad disponible. Si no hay productos registrados, muestra un     mensaje.

▹ salir_programa(): muestra un mensaje de despedida al seleccionar la opción de salida.

5. Uso de listas paralelas
El programa utiliza dos listas: productos y cantidades. Ambas se relacionan mediante sus índices, de manera que el elemento ubicado en una posición de la lista productos corresponde a la cantidad que ocupa esa misma posición en cantidades.

Ejemplo, si productos[0] contiene "Arroz", entonces cantidades[0] contiene la cantidad disponible de arroz. Al modificar o eliminar un producto, se actualiza la lista de cantidades en la misma posición para mantener la información relacionada correctamente.
