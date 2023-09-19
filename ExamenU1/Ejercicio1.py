#Crear una matriz(lista de listas) de n x n donde n >= 2 y n <= 10 
# se creara una funcion que llene la matriz de manera automatica, despues crear una funcion donde
# en forma de caracol empezando por (0,0) se copien los numeros de la matriz llenada automaticamente
# sin ingresar ningun dato en la matriz pero en orden de menor a 

def generar_matriz(n):
    # Crear una matriz de tamaño n x n llena de ceros.
    matriz = [[0 for _ in range(n)] for _ in range(n)]
    # Inicializar variables para rastrear la capa actual y la posición actual.
    nivel = 0
    pos = 0

    # Llenar la matriz siguiendo un patrón específico mientras haya posiciones disponibles.
    while pos < n * n:
        # Calcular cuántos números se colocarán en la capa actual.
        num = n - (nivel * 2) - 1
        temPos = pos

        # Llenar la matriz en las cuatro direcciones desde la posición actual.
        for i in range(num):
            temPos += 1
            matriz[nivel][i + nivel] = temPos          # Arriba
            matriz[nivel + i][n - nivel - 1] = temPos + num  # Derecha
            matriz[n - nivel - 1][n - nivel - i - 1] = temPos + num * 2  # Abajo
            matriz[n - nivel - i - 1][nivel] = temPos + num * 3  # Izquierda

            # Si num es 2, coloca un último número en una posición específica.
            if num == 2:
                matriz[n - nivel - i - 1][nivel + 1] = temPos + num * 3 + 1
                pos += 1

        # Mover a la siguiente capa y posición.
        nivel += 1
        pos += num * 4

    # Devolver la matriz completa.
    return matriz

def imprimir_matriz(matriz):
    # Imprimir la matriz de manera ordenada.
    for fila in matriz:
        for elemento in fila:
            # Imprimir cada elemento en un campo de 3 caracteres.
            print('%3s' % elemento, end='')
        print("")

if __name__ == "__main__":
    # Solicitar al usuario el tamaño de la matriz.
    n = int(input("Ingrese el tamaño de la matriz: "))
    # Generar la matriz y luego imprimirla.
    matriz_generada = generar_matriz(n)
    imprimir_matriz(matriz_generada)