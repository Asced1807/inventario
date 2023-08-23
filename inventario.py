inventario = {} #creamos un diccionario para guardar el inventario

def agregar_producto(nombre_producto, cantidad, precio):
    if nombre_producto in inventario:
        print(f"El producto '{nombre_producto}' ya existe en el inventario.")
    else:
        inventario[nombre_producto] = {'cantidad': cantidad, 'precio': precio}
        print(f"El producto '{nombre_producto}' se agregó correctamente al inventario.")

def eliminar_producto(nombre_producto):
    if nombre_producto in inventario:
        del inventario[nombre_producto]
        print(f"El producto '{nombre_producto}' se eliminó correctamente del inventario.")
    else:
        print(f"El producto '{nombre_producto}' no existe en el inventario.")

def actualizar_cantidad(nombre_producto, cantidad):
    if nombre_producto in inventario:
        inventario[nombre_producto]['cantidad'] = cantidad
        print(f"La cantidad del producto '{nombre_producto}' se actualizó correctamente en el inventario.")
    else:
        print(f"El producto '{nombre_producto}' no existe en el inventario.")

def actualizar_precio(nombre_producto, precio):
    if nombre_producto in inventario:
        inventario[nombre_producto]['precio'] = precio
        print(f"El precio del producto '{nombre_producto}' se actualizó correctamente en el inventario.")
    else:
        print(f"El producto '{nombre_producto}' no existe en el inventario.")

def imprimir_inventario():
    print("{:20} {:<10} {:<10}".format('Nombre del producto', 'Cantidad', 'Precio'))
    print("-"*50)
    for nombre_producto, datos in inventario.items():
        cantidad = datos['cantidad']
        precio = datos['precio']
        print("{:20} {:<10} ${:<10}".format(nombre_producto, cantidad, precio))

# Ejemplo de uso
agregar_producto('Manzanas', 20, 1.50)
agregar_producto('Peras', 10, 2.00)
actualizar_cantidad('Manzanas', 25)
actualizar_precio('Peras', 1.75)
imprimir_inventario()
eliminar_producto('Peras')
agregar_producto('uvas', 20, 1.50)
imprimir_inventario()
