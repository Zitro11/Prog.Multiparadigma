import csv

def leer_csv(nombre_archivo):
    with open(nombre_archivo, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data

def escribir_csv(nombre_archivo, data):
    with open(nombre_archivo, mode='w', newline='') as file:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    directorio = r'C:\Users\melis\Documents\Andy\9NO\Prog.Multiparadigma\ExamenU1\Ejercicio4\\'  # Ruta del directorio

    archivo_original = input("Ingrese el nombre del archivo CSV de entrada: ")
    archivo_actualizado = input("Ingrese el nombre del archivo CSV de salida: ")

    # Combina la ruta del directorio con los nombres de archivo ingresados por el usuario
    ruta_archivo_original = directorio + archivo_original
    ruta_archivo_actualizado = directorio + archivo_actualizado

    data = leer_csv(ruta_archivo_original)
    productos_copiados = []

    for producto in data:
        nombre_producto = producto['Nombre del producto']

        # Buscar productos con el mismo nombre en la lista de productos copiados
        productos_similares = [p for p in productos_copiados if p['Nombre del producto'] == nombre_producto]

        if productos_similares:
            # Hay productos similares, verificar diferencias en precio y cantidad mínima
            for p in productos_similares:
                if p['Precio'] != producto['Precio'] or p['Cantidad minima a comprar'] != producto['Cantidad minima a comprar']:
                    print(f"Diferencia encontrada para el producto '{nombre_producto}':")
                    print(f"1. Precio: {p['Precio']} | 2. Precio: {producto['Precio']}")
                    print(f"1. Cantidad Minima: {p['Cantidad minima a comprar']} | 2. Cantidad Minima: {producto['Cantidad minima a comprar']}")
                    
                    while True:
                        eleccion = input("Seleccione qué valor desea conservar (1 o 2): ")
                        if eleccion in ['1', '2']:
                            # Actualizar el producto en la lista con el valor elegido
                            if eleccion == '1':
                                producto['Precio'] = p['Precio']
                                producto['Cantidad minima a comprar'] = p['Cantidad minima a comprar']
                            break
                        else:
                            print("Opción inválida. Seleccione 1 o 2.")

        else:
            # No hay productos similares, agregar el producto a la lista de productos copiados
            productos_copiados.append(producto)

    # Guardar los datos actualizados en el nuevo archivo CSV
    escribir_csv(ruta_archivo_actualizado, productos_copiados)
    print(f'Productos copiados y guardados en {ruta_archivo_actualizado}')
