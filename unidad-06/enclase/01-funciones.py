






# Unidad 6: Funciones

# ¿Qué es una función?
# Una función es un bloque de código diseñado para resolver un trabajo específico.
# Se agrupa bajo un nombre y puede ser utilizada en diferentes partes del programa.

# Ventajas de usar funciones:
# - Organizar el código en partes más pequeñas y manejables.
# - Mejorar la legibilidad del código.
# - Facilitar el mantenimiento y la reutilización.
# - Permitir la descomposición de problemas grandes en subproblemas más pequeños.

# Ejemplo conceptual:
# Si un código se vuelve muy largo y difícil de entender, podemos dividirlo en funciones más pequeñas.
# Cada función debe resolver una tarea específica.

# (Este script es solo teórico, no tiene ejecución de código.)




   
# Funciones. Nuestra primer función.

#  Acá voy definiendo todas las funciones que voy a usar en el programa


def imprimir_pantalla( texto_a_imprimir ):
    print(texto_a_imprimir)
    pass

texto = "Hola Mundo, pasando parametros!"
imprimir_pantalla(texto)

# Salida en Consola:
# Hola Mundo, pasando parametros!



# Otro ejemplo de función

def texto_ingrese_valor():
    print("--------------------")
    print("Ingrese un valor: ")
    print("--------------------")


texto_ingrese_valor()
valor_uno = input()
texto_ingrese_valor()
valor_dos = input()
print(f"El valor uno es: {valor_uno}, y el valor dos es: {valor_dos}")



















































