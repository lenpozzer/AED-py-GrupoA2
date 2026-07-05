# GESTIÓN DE SUPERMERCADO

ventas_totales = 0
cantidad_ventas = 0
productos_vendidos = {}

# Funciones

def solicitar_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
            else:
                print("Error: debe ingresar un número mayor que cero.")
        except ValueError:
            print("Error: ingrese un número válido.")


def solicitar_float(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            else:
                print("Error: debe ingresar un valor mayor que cero.")
        except ValueError:
            print("Error: ingrese un número válido.") 
            def cargar_productos():
    productos = []

    cantidad = solicitar_entero(
        "\n¿Cuántos productos desea cargar?: "
    )

    for i in range(cantidad):

        print(f"\nProducto {i+1}")

        nombre = input("Nombre: ").strip()

        precio = solicitar_float("Precio: $")

        cantidad_prod = solicitar_entero("Cantidad: ")

        subtotal = precio * cantidad_prod

        productos.append({
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad_prod,
            "subtotal": subtotal
        })

    return productos


def calcular_total(productos):

    total = 0

    for producto in productos:
        total += producto["subtotal"]

    return total


def aplicar_descuento(total):

    descuento = 0

    if total >= 50000:
        descuento = total * 0.15

    elif total >= 20000:
        descuento = total * 0.10

    total_final = total - descuento

    return descuento, total_final


def registrar_productos(productos):

    for producto in productos:

        nombre = producto["nombre"]

        if nombre in productos_vendidos:
            productos_vendidos[nombre] += producto["cantidad"]
        else:
            productos_vendidos[nombre] = producto["cantidad"]
            