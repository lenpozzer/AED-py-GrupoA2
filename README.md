INTEGRANTES DEL GRUPO:
Marichich Speroni, Tobias Santiago
Almeida Diaz, Marcelo Ariel
Bertran Parodi, Joaquin
Bejarano Pozzer, Valentina
Mecozzi, Bianca
*COMISIÓN:
K1.1
*IA UTILIZADA
Claude: Esta IA fue utilazada para corroborar posibles errores en nuestro código y poder estructurarlo mejor en caso de que así se requiriese.
*DESCRIPCIÓN GENERAL DEL SISTEMA
Este proyecto consiste en un sistema por consola desarrollado en Python, orientado a resolver la gestión del flujo de ventas y el control de caja de un supermercado. El programa está estructurado en base a un menú principal interactivo que permite al usuario operar el sistema de forma continua hasta que decida finalizar la ejecución.
Para el desarrollo se aplicaron conceptos de lógica de programación como estructuras de control de flujo, diccionarios para el almacenamiento de datos en memoria, y manejo de excepciones.
 Características principales:
1. Carga Estructurada de Ventas: El sistema permite ingresar un número indefinido de productos por transacción. Para cada producto se solicita el nombre, el precio unitario y la cantidad.
2. Validación de Datos (Manejo de Errores): Se implementaron bloques `try-except` para asegurar que el usuario ingrese únicamente valores numéricos válidos (mayores a cero) en los campos de precio y cantidad, evitando que el programa se rompa por errores de tipeo.
3. Cálculo y Política de Descuentos: 
   * Se evalúa el subtotal de la compra.
   * Si el monto iguala o supera los $20.000, se aplica un 10% de descuento.
   * Si el monto iguala o supera los $50.000, se aplica un 15% de descuento.
4. Emisión de Comprobante (Ticket): Al finalizar la carga de productos, el sistema imprime por consola un ticket detallado que muestra los artículos comprados con sus respectivos subtotales, el descuento aplicado (si corresponde) y el total final a abonar.
5. Generación de Estadísticas: El programa mantiene un registro global de la sesión. Desde el menú principal se puede consultar en cualquier momento:
   * La cantidad total de ventas realizadas.
   * La facturación total acumulada en la sesión.
   * El producto más vendido, calculado mediante el procesamiento del diccionario de artículos registrados.
*INSTRUCCIONES DE EJECUCIÓN
Para poder ejecutar este sistema, es requisito tener instalado un intérprete de Python 3 en el equipo. Las bibliotecas utilizadas son nativas, por lo que no se requiere la instalación de dependencias externas.
Pasos para la ejecución:
1. Guardar el archivo:
   Asegurarse de que el código fuente esté guardado en un archivo con la extensión `.py`

2. Abrir la consola o terminal en caso:
   * En Windows: Presionar la tecla `Windows + R`, escribir `cmd` y presionar Enter.
   * En macOS / Linux: Abrir la aplicación de `Terminal`.

3. Navegar al directorio del proyecto:
   Utilizar el comando `cd` para posicionarse en la carpeta donde se encuentra el archivo Python.
   ```bash
   cd ruta/de/la/carpeta/del/proyecto
