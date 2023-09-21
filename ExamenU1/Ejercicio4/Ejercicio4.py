#Crear un programa que lea del teclado el nombre de un archivo en formato .csv(Productos.csv)
# , para que al menos con 20 lineas de entrada realice lo siguiente mediante una funcion:
# Crear un segundo archivo con el nombre libre a elegir, que sera el llenado en base a lo siguiente:
# Nombre de producto en caso de existir otro producto con el mismo nombre se realizara lo siguiente:
# Verificar si hay diferencias en el 'precio' o 'cantidad minima a comprar',de ser asi pedirle al usuario
# mediante la consola elegir uno de los 2 valores a conservar y solo mostrar una linea del producto con los
# valores modificados

import csv

def leer_csv(nombre_archivo):
    with open(nombre_archivo, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data

def escribir_csv(nombre_archivo, data):
    with open(nombre_archivo, mode='w+', newline='') as file:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def copiar_producto(data, nombre_producto):
    productos_encontrados = []
    for producto in data:
        if producto['Nombre del producto'] == nombre_producto:
            productos_encontrados.append(producto)
    
    if len(productos_encontrados) == 0:
        return None  # No se encontró el producto
    elif len(productos_encontrados) == 1:
        return productos_encontrados[0]  # Solo hay un producto encontrado
    else:
        # Hay múltiples productos con el mismo nombre, mostrar y permitir al usuario elegir
        print(f"Se encontraron {len(productos_encontrados)} productos con el nombre '{nombre_producto}':")
        for i, producto in enumerate(productos_encontrados, start=1):
            print(f"{i}. Producto: {producto}")
        
        while True:
            try:
                opcion = int(input(f"Ingrese el número del producto que desea copiar (1-{len(productos_encontrados)}): "))
                if 1 <= opcion <= len(productos_encontrados):
                    return productos_encontrados[opcion - 1]  # Retornar el producto seleccionado
                else:
                    print("Opción inválida. Ingrese un número válido.")
            except ValueError:
                print("Opción inválida. Ingrese un número válido.")

if __name__ == "__main__":
    archivo_original = r'C:\Users\melis\Documents\Andy\9NO\Prog.Multiparadigma\ExamenU1\Ejercicio4\Productos.csv'
    archivo_actualizado = r'C:\Users\melis\Documents\Andy\9NO\Prog.Multiparadigma\ExamenU1\Ejercicio4\Salida.csv'

    data = leer_csv(archivo_original)
    productos_copiados = []

    while True:
        # Solicitar al usuario el nombre del producto a copiar
        nombre_producto = input("Ingrese el nombre del producto que desea copiar (o 'fin' para terminar): ")
        
        if nombre_producto.lower() == 'fin':
            break  # Salir del bucle si el usuario ingresa 'fin'
        
        producto_copiado = copiar_producto(data, nombre_producto)

        if producto_copiado:
            # Agregar el producto copiado a la lista de productos copiados
            productos_copiados.append(producto_copiado)
        else:
            print(f'El producto "{nombre_producto}" no se encontró en el archivo original.')

    # Guardar los datos actualizados en el nuevo archivo CSV
    escribir_csv(archivo_actualizado, productos_copiados)
    print(f'Productos copiados y guardados en {archivo_actualizado}')
