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
            def imprimir_ticket(productos, total,
                     descuento, total_final):

    print("\n========================")
    print("      SUPERMERCADO")
    print("========================")

    for producto in productos:

        print(
            f"{producto['nombre']} "
            f"x{producto['cantidad']} "
            f"= ${producto['subtotal']:.2f}"
        )

    print("------------------------")
    print(f"Total: ${total:.2f}")
    print(f"Descuento: ${descuento:.2f}")
    print(f"TOTAL A PAGAR: ${total_final:.2f}")
    print("========================\n")


def mostrar_estadisticas():

    print("\n===== ESTADÍSTICAS =====")

    print("Cantidad de ventas:", cantidad_ventas)
    print(f"Facturación total: ${ventas_totales:.2f}")

    if productos_vendidos:

        producto_top = max(
            productos_vendidos,
            key=productos_vendidos.get
        )

        print(
            "Producto más vendido:",
            producto_top,
            f"({productos_vendidos[producto_top]} unidades)"
        )

    else:
        print("No hay ventas registradas.")

    print("========================\n")



# Programa Principal

while True:

    print("====== SUPERMERCADO ======")
    print("1. Nueva venta")
    print("2. Ver estadísticas")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        productos = cargar_productos()

        total = calcular_total(productos)

        descuento, total_final = aplicar_descuento(total)

        imprimir_ticket(
            productos,
            total,
            descuento,
            total_final
        )

        registrar_productos(productos)

        ventas_totales += total_final
        cantidad_ventas += 1

    elif opcion == "2":

        mostrar_estadisticas()

    elif opcion == "3":

        print("Gracias por utilizar el sistema.")
        break

    else:

        print("Opción inválida.\n")