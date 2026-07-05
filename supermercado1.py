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