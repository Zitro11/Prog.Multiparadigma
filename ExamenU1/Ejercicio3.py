class Locacion:
    def __init__(self, nombre, porcentaje_iva):
        self.nombre = nombre
        self.porcentaje_iva = porcentaje_iva
        self.items = []
    
    def __str__(self):
        return self.nombre

    def agregar_item(self, item):
        if item in self.items:
            print("El item ya existe")
        else:
            self.items.append(item)
            print("Item agregado con exito")

    def total_capital(self):
        total = 0
        for item in self.items:
            total += item.precio
        return total

class Item:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
    
    def __str__(self):
        return self.nombre
    
    def __eq__(self, otro):
        return self.nombre == otro.nombre and self.cantidad == otro.cantidad
    def precio(self, porcentaje_iva):
        return self.precio * porcentaje_iva
    
def main():
    locacion = Locacion("Locacion 1", 1.16)
    item1 = Item("Item 1", 1, 100)
    item2 = Item("Item 2", 2, 200)
    item3 = Item("Item 3", 3, 300)
    item4 = Item("Item 4", 4, 400)
    item5 = Item("Item 5", 5, 500)
    item6 = Item("Item 6", 6, 600)
    item7 = Item("Item 7", 7, 700)
    item8 = Item("Item 8", 8, 800)
    item9 = Item("Item 9", 9, 900)
    item10 = Item("Item 10", 10, 1000)
    locacion.agregar_item(item1)
    locacion.agregar_item(item2)
    locacion.agregar_item(item3)
    locacion.agregar_item(item4)
    locacion.agregar_item(item5)
    locacion.agregar_item(item6)
    locacion.agregar_item(item7)
    locacion.agregar_item(item8)
    locacion.agregar_item(item9)
    locacion.agregar_item(item10)
    print(locacion.total_capital())
main()